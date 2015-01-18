# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication

from core.gui.ui_widget_analyse_tweets import Ui_widget_analyse_tweets
from core.gui.widget_wordcloud import WidgetWordcloud
from core.gui.widget_wordcloud_per_cluster import WidgetWordcloudPerCluster
from core.gui.widget_ngrams import widgetNGrams

import os
import pickle
import csv
import sys

class WidgetAnalyseTweets(QWidget, Ui_widget_analyse_tweets):
    """This widget contain gui elements for displaying text analysis over Twitter text data.
    
    The textual analysis include: sentiment analysis (proportion of positive and negative sentiment), 
    cluster analysis, wordclouds and statiscal information about ngram distribution along time.        
    
    Atributes
    -------
    hashtags : dict
        Map hashtags to frequencies.

    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text).

    dataset_top_ngrams : list of tuples (string, number)
        The global importance of each ngram in a text corpus in descending order. 

    top_ngrams_per_cluster : list of lists of tuples (string, number)
        List containing k lists, each one containing max_ngrams_per_cluster tuples
        (ngram, weight), where weight is the centroid component value depicting
        its importance.

    file_name : string
        Dataset name that is being handle. This is the base name for the raw tweets,
        hashtags and wordcloud files.

    regenerate_files : list
        Contains file names that need to be regenarated in case a new dataset is selected.
    """
    def __init__(self):

        QWidget.__init__(self)

        self.regenerate_files = []

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # for some reason not loading icons correctly inside qt designer
        self.button_open_file.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\open.png")))

        self.button_n_grams.setDisabled(True)
        self.button_n_grams_per_cluster.setDisabled(True)
        self.button_relevant_tweets.setDisabled(True)
        self.button_relevant_tweets_per_cluster.setDisabled(True)
        self.button_sentiment.setDisabled(True)
        self.button_sentiment_per_cluster.setDisabled(True)
        self.button_wordcloud.setDisabled(True)
        self.button_wordcloud_per_cluster.setDisabled(True)
        self.button_retweets.setDisabled(True)
        self.button_retweets_per_cluster.setDisabled(True)
        self.button_hashtags.setDisabled(True)
        self.button_hashtags_per_cluster.setDisabled(True)

        # custom event handling
        self.button_open_file.clicked.connect(self.open_tweets_file)
        self.button_wordcloud.clicked.connect(self.add_wordcloud_widget)
        self.button_wordcloud_per_cluster.clicked.connect(self.add_wordcloud_per_cluster_widget)
        self.button_n_grams.clicked.connect(self.add_ngrams_widget)
        self.button_n_grams_per_cluster.clicked.connect(self.add_ngrams_per_cluster_widget)
        
    def add_ngrams_widget(self):
        """Add the n-gram widget to the main layout in response of a click event."""

        self.clear_layout()
        widget_ngrams = widgetNGrams(self.tweets, self.file_name, self.regenerate_files)
       
        self.vlayout_content.addWidget(widget_ngrams)

    def add_ngrams_per_cluster_widget(self):
        """Add the n-gram per cluster widget to the main layout in response of a click event."""

        self.clear_layout()

    def add_wordcloud_widget(self):
        """Add the wordcloud widget to the main layout in response of a click event."""
        
        self.clear_layout()
       
        widget_wordcloud = WidgetWordcloud(self.file_name)
        self.vlayout_content.addWidget(widget_wordcloud)

    def add_wordcloud_per_cluster_widget(self):
        """Add the wordcloud per cluster widget to the main layout in response of a click event."""
        
        self.clear_layout()
        tweets = [t[2] for t in self.tweets]

        # Calculate from wich cluster each tweet belongs to
        tweets_per_cluster = {}
        for tweet, label in zip(tweets, self.cluster_labels):
            if label in tweets_per_cluster:
                tweets_per_cluster[label].append(tweet)
            else:
                tweets_per_cluster[label] = [tweet]

        widget_wordcloud_per_cluster = WidgetWordcloudPerCluster(tweets_per_cluster, self.file_name, 
                                                                 self.regenerate_files)
        self.vlayout_content.addWidget(widget_wordcloud_per_cluster)

    def open_tweets_file(self):
        """Open a csv file containing Twitter text data that will be analysed in response of a click event.
        
        Notes
        -------
        Each csv file has also a binary file associated that contains hashtags
        stored in a dict format.
        """
            
        # user chosen file 
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open data", os.getcwd() + "\\clusterized_tweets\\", "*.csv")
        
        self.tweets = []
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.tweets.append((tweet[0], tweet[1], tweet[2], tweet[3]))

        # loading hashtags
        with open(file_name[:-4] + '_hashtags.pkl', 'rb') as input:
            self.hashtags = pickle.load(input)

        # loading top ngrams per cluster
        with open(file_name[:-4] + '_top_ngrams_per_cluster.pkl', 'rb') as input:
            self.top_ngrams_per_cluster = pickle.load(input)
            
        # loading dataset top ngrams
        with open(file_name[:-4] + '_dataset_top_ngrams.pkl', 'rb') as input:
            self.dataset_top_ngrams = pickle.load(input) 

        self.file_name = file_name[:-4].split("/clusterized_tweets/")[1]

        self.regenerate_files = []

        self.button_n_grams.setDisabled(False)
        self.button_n_grams_per_cluster.setDisabled(False)
        self.button_relevant_tweets.setDisabled(False)
        self.button_relevant_tweets_per_cluster.setDisabled(False)
        self.button_sentiment.setDisabled(False)
        self.button_sentiment_per_cluster.setDisabled(False)
        self.button_wordcloud.setDisabled(False)
        self.button_wordcloud_per_cluster.setDisabled(False)
        self.button_retweets.setDisabled(False)
        self.button_retweets_per_cluster.setDisabled(False)
        self.button_hashtags.setDisabled(False)
        self.button_hashtags_per_cluster.setDisabled(False)

    def clear_layout(self):
        """Remove all the widgets from the main layout."""
        while self.vlayout_content.count():
            child = self.vlayout_content.takeAt(0)
            child.widget().deleteLater()