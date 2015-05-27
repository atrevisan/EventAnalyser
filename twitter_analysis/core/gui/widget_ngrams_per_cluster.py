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

from core.gui.ui_widget_ngrams_per_cluster import Ui_widget_ngrams_per_cluster
from core.textutils.text_analysis import TwitterDataAnalysis, PlotGenerator

class WidgetNGramsPerCluster(QWidget, Ui_widget_ngrams_per_cluster):
    """This widget displays n-grams frequency, retweet and sentiment distributions.
    
    Atributes
    ---------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).

    chosen_cluster_tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).

    top_ngrams_per_cluster : list of lists of tuples (string, number)
        List containing k lists, each one containing max_ngrams_per_cluster tuples
        (ngram, weight), where weight is the centroid component value. 

    clusterized_dataset_path : string
        The path to the clusterized tweets. This path will be used to composing the file name for the plots.

    ngram : string
        The current chosen n-gram for analysis.

    year : string
        The year chosen by the user in the combo box. The distribution info for the chosen ngram
        will take place throughout the months in the chosen year that are present in the clusterized
        tweets corpus.

    month : string
        The month chosen by the user in the combo box. The distribution info for the chosen ngram
        will take place troughout the days in the chosen month.

    tokenize : callable
        Function that handles tokenization of text documents in its contitutent features (n-grams). 

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
 
        # Loading top n-grams per cluster
        with open(self.clusterized_dataset_path[:-4] + "_top_ngrams_per_cluster.pkl", 'rb') as handle:
            self.top_ngrams_per_cluster = pickle.loads(handle.read())
        
        # Loading the feature extractor used in the clustering procedure
        with open(self.clusterized_dataset_path[:-4] + "_feature_extractor.pkl", 'rb') as handle:
            clustering_feature_extractor = pickle.loads(handle.read())

        # Loading the sentiment classification model
        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf" 
        with open(sentiment_classification_model_path_file, 'rb') as handle:
            sentiment_classification_model_path = pickle.loads(handle.read())

        with open(sentiment_classification_model_path, 'rb') as handle:
            self.sentiment_classification_model = pickle.loads(handle.read())

        with open(sentiment_classification_model_path[:-14] + "feature_extractor.pkl", 'rb') as handle:
            self.sentiment_classification_feature_extractor = pickle.loads(handle.read())

        self.tokenize = clustering_feature_extractor.vectorizer.build_analyzer()

        self.plot_generator = PlotGenerator()
        
        self.combo_ngrams.activated[str].connect(self.on_activated_combo_ngrams)

        self.combo_year.activated[str].connect(self.on_activated_combo_year)
        self.combo_month.activated[str].connect(self.on_activated_combo_month)
        self.combo_day.activated[str].connect(self.on_activated_combo_day)

        number_of_clusters = len(self.top_ngrams_per_cluster)
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

        self.combo_ngrams.clear()
        self.combo_ngrams.addItems([ngram[0] for ngram in self.top_ngrams_per_cluster[cluster_label]])

        self.chosen_cluster_tweets = [tweet for tweet in self.tweets if tweet[0] == str(cluster_label)]
        self.twitter_data_analyser = TwitterDataAnalysis(self.chosen_cluster_tweets)

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

    def on_activated_combo_ngrams(self, ngram):
        """Handle events on the combo box n-grams.

        Enable combo year and fill in the available years. Also enables
        the button info per month.
        
        Parameters
        ----------
        ngram : string
            The n-gram chosen by the user in the combo box.
        """

        self.ngram = ngram

        self.combo_year.setDisabled(False)
        self.button_info_per_month.setDisabled(False)

    def on_activated_combo_year(self, year):
        """Handle event on the combo box year.
        
        Sets the chosen year variable. The respective seted value will
        be used to generate the n-gram distribution troughout
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
        be used to generate the n-gram distribution troughout
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
        be used to generate the n-gram distribution troughout
        the hours of the day.

        day : str
            The day chosen by the user in the combo box.
        """

        self.day = day

    def generate_and_plot_info(self, ngram_info, x_label, y_label, title, x_ticks=[], min_x=0, max_x=0):
        """Generate the infos for the ngram and plot it.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen ngram (namely absolute frequency, mean frequency and max frequency).

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
 
        y_total = [total for (month, total, average, max) in ngram_info]
        x_total = [month for (month, total, average, max) in ngram_info]

        y_average = [average for (month, total, average, max) in ngram_info]
        x_average = [month for (month, total, average, max) in ngram_info]

        y_max = [max for (month, total, average, max) in ngram_info]
        x_max = [month for (month, total, average, max) in ngram_info]
            
        max_y = sorted ([total for (month, total, average, max) in ngram_info], key=lambda x : -x)[0]
            
        plot_file_name = self.clusterized_dataset_path[:-4] + "_" + self.ngram.replace(" ", "_") + ".png"
        self.plot_generator.create_three_plots(plot_file_name, 
                                               x_total, y_total, "total", 
                                               x_average, y_average, "average", 
                                               x_max, y_max, "max", 
                                               x_label, y_label, title, 
                                               max_y, min_x=min_x, max_x=max_x, x_ticks=x_ticks)  
         
        self.plot_figure(plot_file_name)

    def generate_info_per_month(self):
        """Generate the infos for the ngram across the months in the chosen year.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen ngram (namely absolute frequency, mean frequency and max frequency).
        """

        x_ticks = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if self.radio_frequency.isChecked():
           
            ngram_info_per_month = self.twitter_data_analyser.generate_ngram_frequency_info_per_month(self.ngram, 
                                                                                                      self.year, 
                                                                                                      self.tokenize)

            ngram_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in ngram_info_per_month]
            ngram_info_per_month = sorted(ngram_info_per_month, key=lambda x : x[0])

            if ngram_info_per_month:
                self.generate_and_plot_info(ngram_info_per_month, "Month", "Frequency", "N-gram frequency", x_ticks)

        elif self.radio_retweets.isChecked():

            ngram_retweets_info_per_month = self.twitter_data_analyser.generate_ngram_retweet_info_per_month(self.ngram,
                                                                                                             self.year,
                                                                                                             self.tokenize)

            ngram_retweets_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in ngram_retweets_info_per_month]
            ngram_retweets_info_per_month = sorted(ngram_retweets_info_per_month, key=lambda x : x[0])

            if ngram_retweets_info_per_month:
                self.generate_and_plot_info(ngram_retweets_info_per_month, "Month", "Frequency", "N-gram retweets", x_ticks)  
                
      
        elif self.radio_positive_sentiment.isChecked():
            
            ngram_positive_sentiment_info_per_month = self.twitter_data_analyser.generate_ngram_sentiment_info_per_month(self.ngram,
                                                                                                                         self.year,
                                                                                                                         self.tokenize,
                                                                                                                         self.sentiment_classification_model,
                                                                                                                         self.sentiment_classification_feature_extractor)

            ngram_positive_sentiment_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in ngram_positive_sentiment_info_per_month]
            ngram_positive_sentiment_info_per_month = sorted(ngram_positive_sentiment_info_per_month, key=lambda x : x[0])

            if ngram_positive_sentiment_info_per_month:
                self.generate_and_plot_info(ngram_positive_sentiment_info_per_month, "Month", "Frequency", "N-gram positive sentiment", x_ticks)

        elif self.radio_negative_sentiment.isChecked():
            
            ngram_negative_sentiment_info_per_month = self.twitter_data_analyser.generate_ngram_sentiment_info_per_month(self.ngram,
                                                                                                                         self.year,
                                                                                                                         self.tokenize,
                                                                                                                         self.sentiment_classification_model,
                                                                                                                         self.sentiment_classification_feature_extractor,
                                                                                                                         sentiment="negative")

            ngram_negative_sentiment_info_per_month = [(x_ticks.index(month) + 1, total, average, max) for month, total, average, max in ngram_negative_sentiment_info_per_month]
            ngram_negative_sentiment_info_per_month = sorted(ngram_negative_sentiment_info_per_month, key=lambda x : x[0])

            if ngram_negative_sentiment_info_per_month:
                self.generate_and_plot_info(ngram_negative_sentiment_info_per_month, "Month", "Frequency", "N-gram negative sentiment", x_ticks)
                     

            
    def generate_info_per_day(self):
        """Generate the infos for the ngram across the days in the chosen month.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen ngram (namely absolute frequency, mean frequency and max frequency).
        """

        if self.radio_frequency.isChecked():
           
            ngram_info_per_day = self.twitter_data_analyser.generate_ngram_frequency_info_per_day(self.ngram, 
                                                                                                  self.month, 
                                                                                                  self.year,
                                                                                                  self.tokenize)

            ngram_info_per_day = [(int(day), total, average, max) for day, total, average, max in ngram_info_per_day]
            ngram_info_per_day = sorted(ngram_info_per_day, key=lambda x : x[0])

            if ngram_info_per_day:
                self.generate_and_plot_info(ngram_info_per_day, "Day", "Frequency", "N-gram frequency", min_x=1, max_x=31)

        elif self.radio_retweets.isChecked():

            ngram_retweets_info_per_day = self.twitter_data_analyser.generate_ngram_retweet__info_per_day(self.ngram,
                                                                                                          self.month,
                                                                                                          self.year,
                                                                                                          self.tokenize)

            ngram_retweets_info_per_day = [(int(day), total, average, max) for day, total, average, max in ngram_retweets_info_per_day]
            ngram_retweets_info_per_day = sorted(ngram_retweets_info_per_day, key=lambda x : x[0])

            if ngram_retweets_info_per_day:
                self.generate_and_plot_info(ngram_retweets_info_per_day, "Day", "Frequency", "N-gram retweets", min_x=1, max_x=31)

        elif self.radio_positive_sentiment.isChecked():

            ngram_positive_sentiment_info_per_day = self.twitter_data_analyser.generate_ngram_sentiment_info_per_day(self.ngram,
                                                                                                                     self.month,
                                                                                                                     self.year,
                                                                                                                     self.tokenize,
                                                                                                                     self.sentiment_classification_model,
                                                                                                                     self.sentiment_classification_feature_extractor)

            ngram_positive_sentiment_info_per_day = [(int(day), total, average, max) for day, total, average, max in ngram_positive_sentiment_info_per_day]
            ngram_positive_sentiment_info_per_day = sorted(ngram_positive_sentiment_info_per_day, key=lambda x : x[0])

            if ngram_positive_sentiment_info_per_day:
                self.generate_and_plot_info(ngram_positive_sentiment_info_per_day, "Day", "Frequency", "N-gram positive sentiment", min_x=1, max_x=31)
            
        elif self.radio_negative_sentiment.isChecked():

            ngram_negative_sentiment_info_per_day = self.twitter_data_analyser.generate_ngram_sentiment_info_per_day(self.ngram,
                                                                                                                     self.month,
                                                                                                                     self.year,
                                                                                                                     self.tokenize,
                                                                                                                     self.sentiment_classification_model,
                                                                                                                     self.sentiment_classification_feature_extractor,
                                                                                                                     sentiment="negative")

            ngram_negative_sentiment_info_per_day = [(int(day), total, average, max) for day, total, average, max in ngram_negative_sentiment_info_per_day]
            ngram_negative_sentiment_info_per_day = sorted(ngram_negative_sentiment_info_per_day, key=lambda x : x[0])

            if ngram_negative_sentiment_info_per_day:
                self.generate_and_plot_info(ngram_negative_sentiment_info_per_day, "Day", "Frequency", "N-gram negative sentiment", min_x=1, max_x=31)

    def generate_info_per_hour(self):
        """Generate the infos for the ngram across the hours in the chosen day.
        
        The info could be the frequency, retweets, positive sentiment or negative sentiment
        relations to the chosen ngram (namely absolute frequency, mean frequency and max frequency).
        """

        if self.radio_frequency.isChecked():
           
            ngram_info_per_hour = self.twitter_data_analyser.generate_ngram_frequency_info_per_hour(self.ngram,
                                                                                                    self.day, 
                                                                                                    self.month,
                                                                                                    self.year, 
                                                                                                    self.tokenize)

            ngram_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in ngram_info_per_hour]
            ngram_info_per_hour = sorted(ngram_info_per_hour, key=lambda x : x[0])

            if ngram_info_per_hour:
                self.generate_and_plot_info(ngram_info_per_hour, "Hour", "Frequency", "N-gram frequency", min_x=0, max_x=23)

        elif self.radio_retweets.isChecked():

            ngram_retweets_info_per_hour = self.twitter_data_analyser.generate_ngram_retweet_info_per_hour(self.ngram,
                                                                                                           self.day,
                                                                                                           self.month,
                                                                                                           self.year,
                                                                                                           self.tokenize)

            ngram_retweets_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in ngram_retweets_info_per_hour]
            ngram_retweets_info_per_hour = sorted(ngram_retweets_info_per_hour, key=lambda x : x[0])

            if ngram_retweets_info_per_hour:
                self.generate_and_plot_info(ngram_retweets_info_per_hour, "Hour", "Frequency", "N-gram retweets", min_x=0, max_x=23)

        elif self.radio_positive_sentiment.isChecked():

            ngram_positive_sentiment_info_per_hour = self.twitter_data_analyser.generate_ngram_sentiment_info_per_hour(self.ngram,
                                                                                                                       self.day,
                                                                                                                       self.month,
                                                                                                                       self.year,
                                                                                                                       self.tokenize,
                                                                                                                       self.sentiment_classification_model,
                                                                                                                       self.sentiment_classification_feature_extractor)

            ngram_positive_sentiment_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in ngram_positive_sentiment_info_per_hour]
            ngram_positive_sentiment_info_per_hour = sorted(ngram_positive_sentiment_info_per_hour, key=lambda x : x[0])

            if ngram_positive_sentiment_info_per_hour:
                self.generate_and_plot_info(ngram_positive_sentiment_info_per_hour, "Hour", "Frequency", "N-gram positive sentiment", min_x=0, max_x=23)

        elif self.radio_negative_sentiment.isChecked():

            ngram_negative_sentiment_info_per_hour = self.twitter_data_analyser.generate_ngram_sentiment_info_per_hour(self.ngram,
                                                                                                                       self.day,
                                                                                                                       self.month,
                                                                                                                       self.year,
                                                                                                                       self.tokenize,
                                                                                                                       self.sentiment_classification_model,
                                                                                                                       self.sentiment_classification_feature_extractor,
                                                                                                                       sentiment="negative")

            ngram_negative_sentiment_info_per_hour = [(int(hour), total, average, max) for hour, total, average, max in ngram_negative_sentiment_info_per_hour]
            ngram_negative_sentiment_info_per_hour = sorted(ngram_negative_sentiment_info_per_hour, key=lambda x : x[0])

            if ngram_negative_sentiment_info_per_hour:
                self.generate_and_plot_info(ngram_negative_sentiment_info_per_hour, "Hour", "Frequency", "N-gram negative sentiment", min_x=0, max_x=23)


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