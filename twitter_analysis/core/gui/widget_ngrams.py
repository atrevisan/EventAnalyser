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

from core.gui.ui_widget_ngrams import Ui_widget_ngrams
from core.textutils.text_analysis import TwitterDataAnalysis, PlotGenerator

class WidgetNGrams(QWidget, Ui_widget_ngrams):
    """This widget displays n-grams frequency, retweet and sentiment distributions.
    
    Atributes
    ---------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text, latitude, longitude).

    dataset_top_ngrams : list of tuples (string, number)
        The global importance of each ngram in a text corpus in descending order. 

    clusterized_dataset_path : string
        The path to the clusterized tweets. This path will be used to composing the file name for the plots.

    ngram : string
        The current chosen n-gram for analysis.

    year : string
        The year chosen by the user in the combo box. The distribution info for the chosen ngram
        will take place throughout the months in the chosen year that are present in the clusterized
        tweets corpus.

    tokenize : callable
        Function that handles tokenization of text documents in its contitutent features (n-grams). 

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
 
        # Loading dataset top n-grams
        with open(self.clusterized_dataset_path[:-4] + "_dataset_top_ngrams.pkl", 'rb') as handle:
            self.dataset_top_ngrams = pickle.loads(handle.read())
        
        # Loading the vectorizer used in the clustering procedure
        with open(self.clusterized_dataset_path[:-4] + "_feature_extractor.pkl", 'rb') as handle:
            clustering_feature_extractor = pickle.loads(handle.read())

        self.tokenize = clustering_feature_extractor.vectorizer.build_analyzer()

        self.twitter_data_analyser = TwitterDataAnalysis(self.tweets)
        self.plot_generator = PlotGenerator()
                               
        self.combo_ngrams.addItems([ngram[0] for ngram in self.dataset_top_ngrams])
        self.combo_ngrams.activated[str].connect(self.on_activated_combo_ngrams)

        self.combo_year.activated[str].connect(self.on_activated_combo_year)
        #self.combo_month.activated[str].connect(self.on_activated_combo_month)
        #self.combo_day.activated[str].connect(self.on_activated_combo_day)

        self.button_info_per_month.clicked.connect(self.generate_info_per_month)
        #self.button_info_per_day.clicked.connect(self.generate_info_per_day)
        #self.button_info_per_hour.clicked.connect(self.generate_info_per_hour)

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
        
        list_of_years = []
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_year = tweet_time.split()[5]
            list_of_years.append(tweet_year)

        self.combo_year.addItems(list(set(list_of_years)))

    def on_activated_combo_year(self, year):
        """Handle event on the combo box year.
        
        Sets the chosen year variable. The respective seted value will
        be used to generate the n-gram distribution troughout
        the months of the year.

        year : str
            The year chosen by the user in the combo box.
        """

        self.year = year

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

            y_total = [total for (month, total, average, max) in ngram_info_per_month]
            x_total = [month for (month, total, average, max) in ngram_info_per_month]

            y_average = [average for (month, total, average, max) in ngram_info_per_month]
            x_average = [month for (month, total, average, max) in ngram_info_per_month]

            y_max = [max for (month, total, average, max) in ngram_info_per_month]
            x_max = [month for (month, total, average, max) in ngram_info_per_month]
            
            max_y = sorted ([total for (month, total, average, max) in ngram_info_per_month], key=lambda x : -x)[0]
            
            plot_file_name = self.clusterized_dataset_path[:-4] + "_" + self.ngram.replace(" ", "_") + ".png"
            self.plot_generator.create_three_plots(plot_file_name, 
                                                   x_total, y_total, "total", 
                                                   x_average, y_average, "average", 
                                                   x_max, y_max, "max", 
                                                   "Month", "Frequency", "N-gram frequncy", 
                                                   max_y, x_ticks=x_ticks)  
         
            self.plot_figure(plot_file_name)   
            
             

    def plot_figure(self, file_name):

        image = QtGui.QImage(file_name)
        pp = QtGui.QPixmap.fromImage(image.scaled(self.label_graph.width(), self.label_graph.height()))
            
        self.label_graph.setPixmap(pp) 

    def generate_ngram_per_hour(self, file_name, ngram):
        """Generate the ngram and ngram per cluster hourly distribution graph.
        
        Parameters
        -----------
        file_name : string
            The file name for the ngram .png graph that will be generated.

        ngram : string
            The ngram from which the hourly frequency distribution graph
            will be generated
        """

        # store the frequency of the given ngram per hour
        ngram_per_hour_frequency = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]

            tweet_tokens = self.analyser(tweet_text)
            hour = tweet_time.split()[3].split(":")[0]

            if hour in ngram_per_hour_frequency:

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_hour_frequency[hour] += 1

            else:
                ngram_per_hour_frequency[hour] = 0

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_hour_frequency[hour] += 1

        # Generate graph plot
        y = [y for x, y in sorted([(int(x), y) for x, y in list(ngram_per_hour_frequency.items())], key=lambda x : x[0])]
        x = [x for x, y in sorted([(int(x), y) for x, y in list(ngram_per_hour_frequency.items())], key=lambda x : x[0])]

        max_frequency = sorted (y, key=lambda x : -x)[0]
        #print("Max frequency: %d" %max_frequency)

        plt.plot(x, y, linewidth=1.5, label=ngram)
        plt.legend()
        plt.axis([0, 23, 0, max_frequency])
        plt.xlabel("Hour")
        plt.ylabel("N-gram frequency")
        plt.title("N-gram frequency distribution")

        plt.savefig(file_name)
        plt.close()

    def generate_ngram_per_day_of_week(self, file_name, ngram):
        """Generate the ngrams and ngrams per cluster day of week distribution graphs.
        
        Parameters
        -----------
        file_name : string
            The base name for the ngrams .png graphs that will be generated.

        ngram : string
            The ngram from wich the day of week distribution graphs
            will be generated
        """

        # store the frequency of the given ngram per day of week
        ngram_per_day_of_week_frequency = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]

            tweet_tokens = self.analyser(tweet_text)
            day_of_week = tweet_time.split()[0]

            if day_of_week in ngram_per_day_of_week_frequency:

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_day_of_week_frequency[day_of_week] += 1

            else:
                ngram_per_day_of_week_frequency[day_of_week] = 0

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_day_of_week_frequency[day_of_week] += 1

        # Generate graph plot
        
        x_ticks = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        ngram_per_day_of_week_frequency = [(x_ticks.index(x), y) for x, y in list (ngram_per_day_of_week_frequency.items())]

        ngram_per_day_of_week_frequency_ordered = sorted(ngram_per_day_of_week_frequency, 
                                                         key=lambda x : x[0])

        y_values = [y for (x, y) in ngram_per_day_of_week_frequency_ordered]
        x_values = [x for (x, y) in ngram_per_day_of_week_frequency_ordered]

        max_frequency = sorted (y_values, key=lambda x : -x)[0]
                
        #print("Max frequency: %d" %max_frequency)

        plt.plot(x_values, y_values, linewidth=1.5, label=ngram)
        plt.legend()
          
        plt.xticks(np.arange(0, 7), x_ticks)
        plt.ylim(0, max_frequency)
                
        plt.xlabel("Day of week")
        plt.ylabel("N-gram frequency")
        plt.title("N-gram frequency distribution")

        plt.savefig(file_name)
        plt.close()

    