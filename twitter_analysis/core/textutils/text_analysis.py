# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

from core.textutils.text_pre_processing import pre_process_tweet_text

class PlotGenerator:
    """Generate and save plot figures for the textual data analysis."""

    def create_three_plots(self, file_name, x1, y1, plot_label1, 
                           x2, y2, plot_label2, x3, y3, plot_label3, 
                           x_label, y_label, title, max_y, x_ticks=[]):
        """Create three plots at the same figure and save it.
        
        Parameters
        ----------
        file_name : string
            The file name for the three plots figure.

        x1 : list of int or float
            The datapoints for the x axis of the first curve.

        y1 : list of int or float
            The datapoints for the y axis of the first curve.

        plot_label1 : str
            The label for the first curve.

        x2 : list of int or float
            The datapoints for the x axis of the second curve.

        y2 : list of int or float
            The datapoints for the y axis of the second curve.

        plot_label2 : str
            The label for the second curve.

        x3 : list of int or float
            The datapoints for the x axis of the third curve.

        y3 : list of int or float
            The datapoints for the y axis of the third curve.

        plot_label3 : str
            The label for the third curve.

        x_label : str
            Label describing the horizontal axis for the plot

        y_label : str
            Label describing the horizontal axis for the plot.
        
        title : str
            The title for the figure.   
            
        x_ticks : list of str
            When the x axis values are text.
            
        max_y : float or int
            Limits the range of values for the vertical axis.
        """

        plt.figure(figsize=(591/96, 450/96), dpi=96)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        plt.plot(x1, y1, linewidth=1.5, label=plot_label1)
        plt.legend()

        plt.plot(x2, y2, linewidth=1.5, label=plot_label2)
        plt.legend()

        plt.plot(x3, y3, linewidth=1.5, label=plot_label3)
        plt.legend()

        if x_ticks:

            plt.xticks(np.arange(1, len(x_ticks)), x_ticks)
        
        plt.ylim(0, max_y)

        plt.savefig(file_name)
        plt.close()

    def create_pie_chart(self, file_name, sizes):
        """Generate a pie chart plot for the percentage of positive/negative tweets.
        
        Parameters
        ----------
        file_name : string
            The file name for the pie chart plot figure.

        sizes : list
            First element: positive sentiment percentage, 
            second element: negative sentiment percentage.
        """

        labels = 'Positive sentiment', 'Negative sentiment'
        colors = ["blue", "red"]

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')

        plt.savefig(file_name)
        plt.close()
        
class TwitterDataAnalysis:
    """Generate plot info regarding n-grams, hashtags and sentiment.
    
    Parameters
    -----------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).
    """

    def __init__(self, tweets):

        self.tweets = tweets

    def generate_dataset_sentiment_info(self, feature_extractor, classifier):
        """Generate the percentage of positive/negative sentiment documents in the whole corpus.
        
        Parameters
        ----------
        feature_extractor : FeatureExtractor
            Reference to the object used to vectorize the training documents used in the sentiment
            classification procedure.

        classifier : document_classification.DocumentClassification object
            Reference to some classification model used to classify the sentiment
            from tweets.

        Returns
        -------
        tuple (float, float) 
            The first element is the percentage of positive sentiment documents
            and the second element is the percentage of negative sentiment documents.
        """
            
        pre_processed_tweets_text = [pre_process_tweet_text(tweet[3]) for tweet in self.tweets]
        test_data = feature_extractor.vectorizer.transform(pre_processed_tweets_text)

        predicted_classes = classifier.predict_document_classes(test_data)

        positive_class_count = predicted_classes.tolist().count(0)
        negative_class_count = predicted_classes.tolist().count(1)

        return (positive_class_count/(positive_class_count + negative_class_count)*100, negative_class_count/(positive_class_count + negative_class_count)*100)


    def generate_dataset_sentiment_info_per_cluster(self, feature_extractor, classifier):
        """Generate the percentage of positive/negative sentiment documents for each cluster of tweets.
        
        Parameters
        ----------
        feature_extractor : FeatureExtractor
            Reference to the object used to vectorize the training documents used in the sentiment
            classification procedure.

        classifier : document_classification.DocumentClassification object
            Reference to some classification model used to classify the sentiment
            from tweets.

        Returns
        -------
        predicted_classes_per_cluster : list of tuples (float, float) 
            The first element is the percentage of positive sentiment documents
            and the second element is the percentage of negative sentiment documents.
        """
        
        tweets_per_cluster = {}

        for tweet in self.tweets:

            if int(tweet[0]) in tweets_per_cluster:

                tweets_per_cluster[int(tweet[0])].append(tweet[3])
            else:

                tweets_per_cluster[int(tweet[0])] = [tweet[3]]
           
        predicted_classes_per_cluster = []

        for cluster_label in tweets_per_cluster:

            pre_processed_tweets_text = [pre_process_tweet_text(tweet) for tweet in tweets_per_cluster[cluster_label]]
            test_data = feature_extractor.vectorizer.transform(pre_processed_tweets_text)

            predicted_classes = classifier.predict_document_classes(test_data)

            positive_class_count = predicted_classes.tolist().count(0)
            negative_class_count = predicted_classes.tolist().count(1)

            predicted_classes_per_cluster.append((positive_class_count/(positive_class_count + negative_class_count)*100, negative_class_count/(positive_class_count + negative_class_count)*100))

        return predicted_classes_per_cluster

    def generate_ngram_frequency_info_per_month(self, ngram, year, tokenize):
        """Generate a mapping for each month of the year to its info.
        
        The infos for a given month regarding a given n-gram are: the n-gram absolute frequency
        in that month, the n-gram mean frequency in that month and the n-gram max frequency
        in that month. The data generated by this function will be used for the plot of the 
        distribution.

        Parameters
        -----------
        ngram : str
            The n-gram for which the distribution will be generated.

        year : str
            The distribution will be generated for the months in this year.

        tokenize : callable
            Function that handles tokenization of text documents in its contitutent features (n-grams). 

        Returns
        --------
        plot_info : list of tuples (str, int, float, int)
            The total, average and max frequency of the n-gram in the month.
        """

        # store the info of the given ngram per month
        ngram_info_per_month = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]
            tweet_tokens = tokenize(tweet_text)
            
            # Do The n-gram belongs to the tweet?
            if ngram in tweet_tokens:
            
                month = tweet_time.split()[1]
                day = tweet_time.split()[2]

                if month in ngram_info_per_month:

                    month_info = ngram_info_per_month[month]
                    ngram_month_frequency = month_info[0]
                    ngram_daily_frequency = month_info[1]

                    ngram_month_frequency += tweet_tokens.count(ngram)
                    
                    if day in ngram_daily_frequency:
                        
                        ngram_daily_frequency[day] +=  tweet_tokens.count(ngram)

                    else:

                        ngram_daily_frequency[day] = tweet_tokens.count(ngram)

                    month_info = (ngram_month_frequency, ngram_daily_frequency)
                    ngram_info_per_month[month] = month_info

                else:

                    ngram_month_frequency = tweet_tokens.count(ngram)
                    ngram_daily_frequency = {}
                    ngram_daily_frequency[day] = tweet_tokens.count(ngram)
                    
                    month_info = (ngram_month_frequency, ngram_daily_frequency)
                    ngram_info_per_month[month] = month_info

        # calculate average and max frequency of the n-gram in the month
        plot_info = []
        for month_item in ngram_info_per_month.items():

            month_info = month_item[1]
            ngram_month_frequency = month_info[0]
            ngram_daily_frequency = month_info[1]

            ngram_average_frequency = ngram_month_frequency / len(ngram_daily_frequency)
            ngram_max_frequency = ngram_daily_frequency[max(ngram_daily_frequency, key=lambda k: ngram_daily_frequency[k])]

            plot_info.append((month_item[0], ngram_month_frequency, ngram_average_frequency, ngram_max_frequency))

        return plot_info

    def generate_ngram_frequency_info_per_day(self, ngram, month, tokenize):
        """Generate a mapping for each day of the month to its info.
        
        The infos for a given day regarding a given n-gram are: the n-gram absolute frequency
        in that day, the n-gram mean frequency in that day and the n-gram max frequency
        in that day. The data generated by this function will be used for the plot of the 
        distribution.

        Parameters
        -----------
        ngram : str
            The n-gram for which the distribution will be generated.

        month : str
            The distribution will be generated for the days in this month.

        tokenize : callable
            Function that handles tokenization of text documents in its features (n-grams). 

        Returns
        --------
        plot_info : list of tuples (str, int, float, int)
            The total, average and max frequency of the n-gram in the day.
        """

        # store the info of the given ngram per day
        ngram_info_per_day = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]
            tweet_tokens = tokenize(tweet_text)
            
            tweet_month = tweet_time.split()[1]

            # Do The n-gram belongs to the tweet?
            if ngram in tweet_tokens and month == tweet_month:
             
                day = tweet_time.split()[2]
                hour = tweet_time.split()[3].split(":")[0]

                if day in ngram_info_per_day:

                    day_info = ngram_info_per_day[day]

                    ngram_day_frequency = day_info[0]
                    ngram_hourly_frequency = day_info[1]

                    ngram_day_frequency += tweet_tokens.count(ngram)
                    
                    if hour in ngram_hourly_frequency:
                        
                        ngram_hourly_frequency[hour] +=  tweet_tokens.count(ngram)

                    else:

                        ngram_hourly_frequency[hour] = tweet_tokens.count(ngram)

                    day_info = (ngram_day_frequency, ngram_hourly_frequency)
                    ngram_info_per_day[day] = day_info

                else:

                    ngram_day_frequency = tweet_tokens.count(ngram)
                    ngram_hourly_frequency = {}
                    ngram_hourly_frequency[hour] = tweet_tokens.count(ngram)
                    
                    day_info = (ngram_day_frequency, ngram_hourly_frequency)
                    ngram_info_per_day[day] = day_info

        # calculate average and max frequency of the n-gram in the day
        plot_info = []
        for day_item in ngram_info_per_day.items():

            day_info = day_item[1]
            ngram_day_frequency = day_info[0]
            ngram_hourly_frequency = day_info[1]

            ngram_average_frequency = ngram_day_frequency / len(ngram_hourly_frequency)
            ngram_max_frequency = ngram_hourly_frequency[max(ngram_hourly_frequency, key=lambda k: ngram_hourly_frequency[k])]

            plot_info.append((day_item[0], ngram_day_frequency, ngram_average_frequency, ngram_max_frequency))

        return plot_info


