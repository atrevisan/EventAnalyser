# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4

import os
import pickle
import csv

from core.gui.ui_widget_hashtags_per_cluster import Ui_widget_hashtags_per_cluster
from core.textutils.text_analysis import TwitterDataAnalysis, PlotGenerator

class WidgetHashtagsPerCluster(QWidget, Ui_widget_hashtags_per_cluster):
    """This widget displays hashtags frequency, retweet and sentiment distributions.
    
    Atributes
    ---------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).

    chosen_cluster_tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).

    clusterized_dataset_path : string
        The path to the clusterized tweets. This path will be used to composing the file name for the plots.

    hashtag : string
        The current chosen hashtag for analysis.

    year : string
        The year chosen by the user in the combo box. The distribution info for the chosen hashtag
        will take place throughout the months in the chosen year that are present in the clusterized
        tweets corpus.

    month : string
        The month chosen by the user in the combo box. The distribution info for the chosen hashtag
        will take place troughout the days in the chosen month.

    sentiment_feature_extractor : FeatureExtractor
            Reference to the object used to vectorize the training documents used in the sentiment
            classification procedure.

    sentiment_classification_model : document_classification.DocumentClassification object
            Reference to some classification model used to classify the sentiment
            from tweets.

    twitter_data_analyser : TwitterDataAnalysis
        Compute statistical informations regarding the tweets.

    plot_generator : PlotGenerator
        Generates and saves various kinds of plots from the infos
        obtained from the twitter_data_analyser.
    """

    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.combo_year.setDisabled(True)
        self.combo_month.setDisabled(True)
        self.combo_day.setDisabled(True)

        self.button_info_per_month.setDisabled(True)
        self.button_info_per_day.setDisabled(True)
        self.button_info_per_hour.setDisabled(True)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            self.clusterized_dataset_path = pickle.loads(handle.read())

        # Loading clusterized tweets
        self.tweets = []
        with open(self.clusterized_dataset_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.tweets.append((tweet[0], tweet[1], tweet[2], tweet[3], tweet[4], tweet[5]))
        
        # Loading the sentiment classification model
        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf" 
        with open(sentiment_classification_model_path_file, 'rb') as handle:
            sentiment_classification_model_path = pickle.loads(handle.read())

        with open(sentiment_classification_model_path, 'rb') as handle:
            self.sentiment_classification_model = pickle.loads(handle.read())

        with open(sentiment_classification_model_path[:-14] + "feature_extractor.pkl", 'rb') as handle:
            self.sentiment_classification_feature_extractor = pickle.loads(handle.read())

        self.plot_generator = PlotGenerator()
        
        self.combo_hashtags.activated[str].connect(self.on_activated_combo_hashtags)

        self.combo_year.activated[str].connect(self.on_activated_combo_year)
        self.combo_month.activated[str].connect(self.on_activated_combo_month)
        self.combo_day.activated[str].connect(self.on_activated_combo_day)

        # Loading top n-grams per cluster
        with open(self.clusterized_dataset_path[:-4] + "_top_ngrams_per_cluster.pkl", 'rb') as handle:
            top_ngrams_per_cluster = pickle.loads(handle.read())

        number_of_clusters = len(top_ngrams_per_cluster)
        self.combo_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(number_of_clusters)])
        self.combo_cluster.activated[int].connect(self.on_activated_combo_cluster)

        self.button_info_per_month.clicked.connect(self.generate_info_per_month)
        self.button_info_per_day.clicked.connect(self.generate_info_per_day)
        self.button_info_per_hour.clicked.connect(self.generate_info_per_hour)

    def on_activated_combo_cluster(self, cluster_label):
        """Filter the tweets that belong to the chosen cluster.
        
        Parameteer
        ----------
        cluster_label : int
            The index of the chosen cluster from the combobox.
        """

        self.combo_hashtags.clear()

        self.chosen_cluster_tweets = [tweet for tweet in self.tweets if tweet[0] == str(cluster_label)]
        self.twitter_data_analyser = TwitterDataAnalysis(self.chosen_cluster_tweets)

        self.combo_hashtags.addItems([hashtag[0] for hashtag in self.twitter_data_analyser.get_top_hashtags()])

        list_of_years = []
        list_of_months = []
        for tweet in self.chosen_cluster_tweets:

            tweet_time = tweet[1]
            tweet_year = tweet_time.split()[5]
            tweet_month = tweet_time.split()[1]
            
            list_of_years.append(tweet_year)
            list_of_months.append(tweet_month)
            
        self.combo_year.clear()
        self.combo_month.clear()

        self.combo_year.addItems(list(set(list_of_years)))
        self.combo_month.addItems(list(set(list_of_months)))

    def on_activated_combo_hashtags(self, hashtag):
        """Handle events on the combo box hashtags.

        Enable combo year and fill in the available years. Also enables
        the button info per month.
        
        Parameters
        ----------
        hashtag : string
            The hashtag chosen by the user in the combo box.
        """

        self.hashtag = hashtag

        self.combo_year.setDisabled(False)
        self.button_info_per_month.setDisabled(False)

    def on_activated_combo_year(self, year):
        """Handle event on the combo box year.
        
        Sets the chosen year variable. The respective seted value will
        be used to generate the hashtag distribution troughout
        the months of the year.

        year : str
            The year chosen by the user in the combo box.
        """

        self.year = year

        self.combo_month.setDisabled(False)
        self.button_info_per_day.setDisabled(False)

    def on_activated_combo_month(self, month):
        """Handle event on the combo box month.
        
        Sets the chosen month variable. The respective seted value will
        be used to generate the hashtag distribution troughout
        the days of the month.

        month : str
            The month chosen by the user in the combo box.
        """

        self.month = month

        self.combo_day.setDisabled(False)
        self.button_info_per_hour.setDisabled(False)

        self.combo_day.clear()

        list_of_days = []
        for tweet in self.chosen_cluster_tweets:

            tweet_time = tweet[1]
            tweet_month = tweet_time.split()[1]

            if tweet_month == self.month:

                tweet_day = tweet_time.split()[2]
                list_of_days.append(tweet_day)
                
        self.combo_day.addItems(sorted(list(set(list_of_days))))

    def on_activated_combo_day(self, day):
        """Handle event on the combo box day.
        
        Sets the chosen day variable. The respective seted value will
        be used to generate the hashtag distribution troughout
        the hours of the day.

        day : str
            The day chosen by the user in the combo box.
        """

        self.day = day

    def generate_and_plot_info(self, hashtag_info, x_label, y_label, title, x_ticks=[], min_x=0, max_x=0):
        """Generate the infos for the hashtag and plot it.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen hashtag (namely absolute frequency, mean frequency and max frequency).

        Parameters
        ----------
        ngram_info : list of tuples (int, int, float, int)
            The x axis component, the total, the average and max
            component values for the three curves.

        x_label : str
            The x axis title.    

        y_label : str
            The y axis title.

        title : str
            The plot title.

        x_ticks : list of str
            The x axis values when strings.

        min_x : int
            The smaller value in the x axis range.

        max_x : int
            The largest value in the x axis range.
        """
 
        y_total = [total for (month, total, average, max) in hashtag_info]
        x_total = [month for (month, total, average, max) in hashtag_info]

        y_average = [average for (month, total, average, max) in hashtag_info]
        x_average = [month for (month, total, average, max) in hashtag_info]

        y_max = [max for (month, total, average, max) in hashtag_info]
        x_max = [month for (month, total, average, max) in hashtag_info]
            
        max_y = sorted ([total for (month, total, average, max) in hashtag_info], key=lambda x : -x)[0]
            
        plot_file_name = self.clusterized_dataset_path[:-4] + "_" + self.hashtag + ".png"
        self.plot_generator.create_three_plots(plot_file_name, 
                                               x_total, y_total, "total", 
                                               x_average, y_average, "average", 
                                               x_max, y_max, "max", 
                                               x_label, y_label, title, 
                                               max_y, min_x=min_x, max_x=max_x, x_ticks=x_ticks)  
         
        self.plot_figure(plot_file_name)

    def clear_plot(self, x_label, y_label, title, x_ticks=[], min_x=0, max_x=0):
        """Clear the plot when no info is generated.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen hashtag (namely absolute frequency, mean frequency and max frequency).

        Parameters
        ----------
        x_label : str
            The x axis title.    

        y_label : str
            The y axis title.

        title : str
            The plot title.

        x_ticks : list of str
            The x axis values when strings.

        min_x : int
            The smaller value in the x axis range.

        max_x : int
            The largest value in the x axis range.
        """
 
        y_total = []
        x_total = []

        y_average = []
        x_average = []

        y_max = []
        x_max = []
            
        max_y = 0
            
        plot_file_name = self.clusterized_dataset_path[:-4] + "_" + self.hashtag + ".png"
        self.plot_generator.create_three_plots(plot_file_name, 
                                               x_total, y_total, "total", 
                                               x_average, y_average, "average", 
                                               x_max, y_max, "max", 
                                               x_label, y_label, title, 
                                               max_y, min_x=min_x, max_x=max_x, x_ticks=x_ticks)  
         
        self.plot_figure(plot_file_name)

    def generate_info_per_month(self):
        """Generate the infos for the hashtag across the months in the chosen year.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen hashtag (namely absolute frequency, mean frequency and max frequency).
        """

        x_ticks = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if self.radio_frequency.isChecked():
           
            hashtag_info_per_month = self.twitter_data_analyser.generate_hashtag_frequency_info_per_month(self.hashtag, 
                                                                                                          self.year) 
                                                                                                      

            hashtag_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in hashtag_info_per_month]
            hashtag_info_per_month = sorted(hashtag_info_per_month, key=lambda x : x[0])

            if hashtag_info_per_month:
                self.generate_and_plot_info(hashtag_info_per_month, "Month", "Frequency", "Hashtag frequency", x_ticks)
            else:
                self.clear_plot("Month", "Frequency", "Hashtag frequency", x_ticks)

        elif self.radio_retweets.isChecked():

            hashtag_retweets_info_per_month = self.twitter_data_analyser.generate_hashtag_retweet_info_per_month(self.hashtag,
                                                                                                                 self.year)
                                                                                                             

            hashtag_retweets_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in hashtag_retweets_info_per_month]
            hashtag_retweets_info_per_month = sorted(hashtag_retweets_info_per_month, key=lambda x : x[0])

            if hashtag_retweets_info_per_month:
                self.generate_and_plot_info(hashtag_retweets_info_per_month, "Month", "Frequency", "Hashtag retweets", x_ticks)
            else:
                self.clear_plot("Month", "Frequency", "Hashtag retweets", x_ticks)  
                
      
        elif self.radio_positive_sentiment.isChecked():
            
            hashtag_positive_sentiment_info_per_month = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_month(self.hashtag,
                                                                                                                             self.year,
                                                                                                                             self.sentiment_classification_model,
                                                                                                                             self.sentiment_classification_feature_extractor)

            hashtag_positive_sentiment_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in hashtag_positive_sentiment_info_per_month]
            hashtag_positive_sentiment_info_per_month = sorted(hashtag_positive_sentiment_info_per_month, key=lambda x : x[0])

            if hashtag_positive_sentiment_info_per_month:
                self.generate_and_plot_info(hashtag_positive_sentiment_info_per_month, "Month", "Frequency", "Hashtag positive sentiment", x_ticks)
            else:
                self.clear_plot("Month", "Frequency", "Hashtag positive sentiment", x_ticks)

        elif self.radio_negative_sentiment.isChecked():
            
            hashtag_negative_sentiment_info_per_month = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_month(self.hashtag,
                                                                                                                             self.year,
                                                                                                                             self.sentiment_classification_model,
                                                                                                                             self.sentiment_classification_feature_extractor,
                                                                                                                             sentiment="negative")

            hashtag_negative_sentiment_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in hashtag_negative_sentiment_info_per_month]
            hashtag_negative_sentiment_info_per_month = sorted(hashtag_negative_sentiment_info_per_month, key=lambda x : x[0])

            if hashtag_negative_sentiment_info_per_month:
                self.generate_and_plot_info(hashtag_negative_sentiment_info_per_month, "Month", "Frequency", "Hashtag negative sentiment", x_ticks)
            else:
                self.clear_plot("Month", "Frequency", "Hashtag negative sentiment", x_ticks)
                     
    def generate_info_per_day(self):
        """Generate the infos for the hashtag across the days in the chosen month.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen hashtag (namely absolute frequency, mean frequency and max frequency).
        """

        if self.radio_frequency.isChecked():
           
            hashtag_info_per_day = self.twitter_data_analyser.generate_hashtag_frequency_info_per_day(self.hashtag, 
                                                                                                      self.month, 
                                                                                                      self.year)
                                                                                                  

            hashtag_info_per_day = [(int(day), total, average, max) for day, total, average, max in hashtag_info_per_day]
            hashtag_info_per_day = sorted(hashtag_info_per_day, key=lambda x : x[0])

            if hashtag_info_per_day:
                self.generate_and_plot_info(hashtag_info_per_day, "Day", "Frequency", "Hashtag frequency", min_x=1, max_x=31)
            else:
                self.clear_plot("Day", "Frequency", "Hashtag frequency", min_x=1, max_x=31)

        elif self.radio_retweets.isChecked():

            hashtag_retweets_info_per_day = self.twitter_data_analyser.generate_hashtag_retweet__info_per_day(self.hashtag,
                                                                                                              self.month,
                                                                                                              self.year)
                                                                                                          

            hashtag_retweets_info_per_day = [(int(day), total, average, max) for day, total, average, max in hashtag_retweets_info_per_day]
            hashtag_retweets_info_per_day = sorted(hashtag_retweets_info_per_day, key=lambda x : x[0])

            if hashtag_retweets_info_per_day:
                self.generate_and_plot_info(hashtag_retweets_info_per_day, "Day", "Frequency", "Hashtag retweets", min_x=1, max_x=31)
            else:
                self.clear_plot("Day", "Frequency", "Hashtag retweets", min_x=1, max_x=31)

        elif self.radio_positive_sentiment.isChecked():

            hashtag_positive_sentiment_info_per_day = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_day(self.hashtag,
                                                                                                                         self.month,
                                                                                                                         self.year,
                                                                                                                         self.sentiment_classification_model,
                                                                                                                         self.sentiment_classification_feature_extractor)

            hashtag_positive_sentiment_info_per_day = [(int(day), total, average, max) for day, total, average, max in hashtag_positive_sentiment_info_per_day]
            hashtag_positive_sentiment_info_per_day = sorted(hashtag_positive_sentiment_info_per_day, key=lambda x : x[0])

            if hashtag_positive_sentiment_info_per_day:
                self.generate_and_plot_info(hashtag_positive_sentiment_info_per_day, "Day", "Frequency", "Hashtag positive sentiment", min_x=1, max_x=31)
            else:
                self.clear_plot("Day", "Frequency", "Hashtag positive sentiment", min_x=1, max_x=31)
            
        elif self.radio_negative_sentiment.isChecked():

            hashtag_negative_sentiment_info_per_day = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_day(self.hashtag,
                                                                                                                         self.month,
                                                                                                                         self.year,
                                                                                                                         self.sentiment_classification_model,
                                                                                                                         self.sentiment_classification_feature_extractor,
                                                                                                                         sentiment="negative")

            hashtag_negative_sentiment_info_per_day = [(int(day), total, average, max) for day, total, average, max in hashtag_negative_sentiment_info_per_day]
            hashtag_negative_sentiment_info_per_day = sorted(hashtag_negative_sentiment_info_per_day, key=lambda x : x[0])

            if hashtag_negative_sentiment_info_per_day:
                self.generate_and_plot_info(hashtag_negative_sentiment_info_per_day, "Day", "Frequency", "Hashtag negative sentiment", min_x=1, max_x=31)
            else:
                self.clear_plot("Day", "Frequency", "Hashtag negative sentiment", min_x=1, max_x=31)

    def generate_info_per_hour(self):
        """Generate the infos for the hashtag across the hours in the chosen day.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen hashtag (namely absolute frequency, mean frequency and max frequency).
        """

        if self.radio_frequency.isChecked():
           
            hashtag_info_per_hour = self.twitter_data_analyser.generate_hashtag_frequency_info_per_hour(self.hashtag,
                                                                                                        self.day, 
                                                                                                        self.month,
                                                                                                        self.year) 
                                                                                                    

            hashtag_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in hashtag_info_per_hour]
            hashtag_info_per_hour = sorted(hashtag_info_per_hour, key=lambda x : x[0])

            if hashtag_info_per_hour:
                self.generate_and_plot_info(hashtag_info_per_hour, "Hour", "Frequency", "Hashtag frequency", min_x=0, max_x=23)
            else:
                self.clear_plot("Hour", "Frequency", "Hashtag frequency", min_x=0, max_x=23)

        elif self.radio_retweets.isChecked():

            hashtag_retweets_info_per_hour = self.twitter_data_analyser.generate_hashtag_retweet_info_per_hour(self.hashtag,
                                                                                                               self.day,
                                                                                                               self.month,
                                                                                                               self.year)
                                                                                                           

            hashtag_retweets_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in hashtag_retweets_info_per_hour]
            hashtag_retweets_info_per_hour = sorted(hashtag_retweets_info_per_hour, key=lambda x : x[0])

            if hashtag_retweets_info_per_hour:
                self.generate_and_plot_info(hashtag_retweets_info_per_hour, "Hour", "Frequency", "Hashtag retweets", min_x=0, max_x=23)
            else:
                self.clear_plot("Hour", "Frequency", "Hashtag retweets", min_x=0, max_x=23)

        elif self.radio_positive_sentiment.isChecked():

            hashtag_positive_sentiment_info_per_hour = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_hour(self.hashtag,
                                                                                                                           self.day,
                                                                                                                           self.month,
                                                                                                                           self.year,
                                                                                                                           self.sentiment_classification_model,
                                                                                                                           self.sentiment_classification_feature_extractor)

            hashtag_positive_sentiment_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in hashtag_positive_sentiment_info_per_hour]
            hashtag_positive_sentiment_info_per_hour = sorted(hashtag_positive_sentiment_info_per_hour, key=lambda x : x[0])

            if hashtag_positive_sentiment_info_per_hour:
                self.generate_and_plot_info(hashtag_positive_sentiment_info_per_hour, "Hour", "Frequency", "Hashtag positive sentiment", min_x=0, max_x=23)
            else:
                self.clear_plot("Hour", "Frequency", "Hashtag positive sentiment", min_x=0, max_x=23)

        elif self.radio_negative_sentiment.isChecked():

            hashtag_negative_sentiment_info_per_hour = self.twitter_data_analyser.generate_hashtag_sentiment_info_per_hour(self.hashtag,
                                                                                                                           self.day,
                                                                                                                           self.month,
                                                                                                                           self.year,
                                                                                                                           self.sentiment_classification_model,
                                                                                                                           self.sentiment_classification_feature_extractor,
                                                                                                                           sentiment="negative")

            hashtag_negative_sentiment_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in hashtag_negative_sentiment_info_per_hour]
            hashtag_negative_sentiment_info_per_hour = sorted(hashtag_negative_sentiment_info_per_hour, key=lambda x : x[0])

            if hashtag_negative_sentiment_info_per_hour:
                self.generate_and_plot_info(hashtag_negative_sentiment_info_per_hour, "Hour", "Frequency", "Hashtag negative sentiment", min_x=0, max_x=23)
            else:
                self.clear_plot("Hour", "Frequency", "Hashtag negative sentiment", min_x=0, max_x=23)


    def plot_figure(self, file_name):
        """Show the generated plot in the gui.
        
        Parameters
        -----------
        file_name : str
            The location to the figure .png file.
        """

        image = QtGui.QImage(file_name)
        pp = QtGui.QPixmap.fromImage(image.scaled(self.label_graph.width(), self.label_graph.height()))
            
        self.label_graph.setPixmap(pp) 