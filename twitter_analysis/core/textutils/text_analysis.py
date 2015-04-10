# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import matplotlib.pyplot as plt

class PlotGenerator:
    """Generate and save plot figures of the textual data analysis."""

    def create_three_plots(self, file_name, x1, y1, plot_label1, 
                           x2, y2, plot_label2, x3, y3, plot_label3, 
                           x_label, y_label, title):
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
        
        title : str
            The title for the figure.    
        """

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        plt.plot(x1, y1, linewidth=1.5, label=plot_label1)
        plt.legend()

        plt.plot(x2, y2, linewidth=1.5, label=plot_label2)
        plt.legend()

        plt.plot(x3, y3, linewidth=1.5, label=plot_label3)
        plt.legend()

        plt.savefig(file_name)
        plt.close()
         

class TwitterDataAnalysis:
    """Generate plot info regarding n-grams and hashtags.
    
    Parameters
    -----------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text).

    tokenizer : callable
        Reference to the function generated by the vectorizer used in the document clustering, 
        this function is used to handle tokenization of text documents.
    """

    def __init__(self, tweets, tokenizer):

        self.tweets = tweets
        self.tokenizer = tokenizer

    def generate_ngram_info_per_month(self, ngram, year):
        """Generate a mapping of the months of the year to the month's info.
        
        The infos for a given month regarding a given n-gram are: n-gram frequency
        in that month, the n-gram mean frequency in that month and the n-gram max frequency
        in that month. The data generated by this function will be used for the plot of the 
        distribution.

        Parameters
        -----------
        ngram : str
            The n-gram for which the distribution will be generated.

        year : str
            The distribution will be generated for the months in this year.

        Returns
        --------
        plot_info : list of 3-tuples (str, int, float, int)
            The total, average and max frequency of the n-gram in the month.
        """

        # store the info of the given ngram per month
        ngram_info_per_month = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]
            tweet_tokens = self.tokenizer(tweet_text)
            
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

                    month_info = [ngram_month_frequency, ngram_daily_frequency]
                    ngram_info_per_month[month] = month_info

                else:

                    ngram_month_frequency = tweet_tokens.count(ngram)
                    ngram_daily_frequency = {}
                    ngram_daily_frequency[day] = tweet_tokens.count(ngram)
                    
                    month_info = [ngram_month_frequency, ngram_daily_frequency]
                    ngram_info_per_month[month] = month_info

        # calculate average and max frequency of the n-gram in the month
        plot_info = []
        for month_item in ngram_info_per_month.items():

            month_info = month_item[1]
            ngram_month_frequency = month_info[0]
            ngram_daily_frequency = month_info[1]

            ngram_average_frequency = ngram_month_frequency / len(ngram_daily_frequency)
            ngram_max_frequency = ngram_daily_frequency[max(ngram_daily_frequency)]

            plot_info.append((month_item[0], ngram_month_frequency, ngram_average_frequency, ngram_max_frequency))

        return plot_info

