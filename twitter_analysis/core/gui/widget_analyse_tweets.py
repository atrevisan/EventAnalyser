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
from core.gui.dialog_generate_clusters import GenerateClustersDialog

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
        Store tweets in the form (created_at, retweet_count, tweet_text).

    labels : list of int [n_samples]
        Store the indexes from witch label each tweet belongs to.

    top_words_per_cluster : list of lists of string [k][max_words_per_cluster]
        Store the top words from each cluster.

    file_name : string
        Dataset name that is being handle. This is the base name for the raw tweets,
        hashtags and wordcloud files.

    regenerate_wordcloud : Boolean
        If a dataset is selected again for clusterization, clusterize the dataset
        and generate a new wordcloud, otherwize use the already existent wordcloud.

    regenerate_wordcloud_per_cluster : dict
        Maps the wordcloud file name of the cluster to if it needs to be regenerated. If a dataset is selected
        again for clusterization, clusterize the dataset and generate a new wordcloud for each cluster, 
        otherwize use the already existent wordclouds. If it is empty it means all wordclouds need to be regenerated.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        self.regenerate_wordcloud = False
        self.regenerate_wordcloud_per_cluster = {}

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # for some reason not loading icons correctly inside designer
        self.button_open_file.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\open.png")))

        self.line_edit_clusters.setDisabled(True)

        self.button_clusterize.setDisabled(True)
        self.button_n_grams.setDisabled(True)
        self.button_n_grams_per_cluster.setDisabled(True)
        self.button_relevant_tweets.setDisabled(True)
        self.button_relevant_tweets_per_cluster.setDisabled(True)
        self.button_sentiment.setDisabled(True)
        self.button_sentiment_per_cluster.setDisabled(True)
        self.button_wordcloud.setDisabled(True)
        self.button_wordcloud_per_cluster.setDisabled(True)
        
        # custom event handling
        self.button_open_file.clicked.connect(self.open_tweets_file)
        self.button_wordcloud.clicked.connect(self.add_wordcloud_widget)
        self.button_wordcloud_per_cluster.clicked.connect(self.add_wordcloud_per_cluster_widget)
        self.button_clusterize.clicked.connect(self.start_clustering)

 
    def start_clustering(self):
        """Invoke the modal dialog that perform the clustering procedure."""

        # desired number of clusters
        k = int(self.line_edit_clusters.text())

        tweets = [tweet[2] for tweet in self.tweets]
        
        self.labels, self.top_words_per_cluster, ok = GenerateClustersDialog.generate_clusters(tweets, k)
        
        self.button_clusterize.setDisabled(False)
        self.button_n_grams.setDisabled(False)
        self.button_n_grams_per_cluster.setDisabled(False)
        self.button_relevant_tweets.setDisabled(False)
        self.button_relevant_tweets_per_cluster.setDisabled(False)
        self.button_sentiment.setDisabled(False)
        self.button_sentiment_per_cluster.setDisabled(False)
        self.button_wordcloud.setDisabled(False)
        self.button_wordcloud_per_cluster.setDisabled(False)

        self.line_edit_clusters.setText("")
        self.line_edit_clusters.setDisabled(True)
        self.button_clusterize.setDisabled(True)

        self.regenerate_wordcloud = True
        self.regenerate_wordcloud_per_cluster = {}

        self.clear_layout()

    def open_tweets_file(self):
        """Open a csv file containing Twitter text data that will be analysed in response of a click event.
        
        Notes
        -------
        Each csv file has also a binary file associated that contains hashtags
        stored in a dict format.
        """
            
        # user chosen file 
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open data", os.getcwd() + "\\tweets\\", "*.csv")
        
        self.tweets = []
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.tweets.append((tweet[0], tweet[1], tweet[2]))

        # loading hashtags
        with open(file_name[:-4] + "_hashtags.txt", 'rb') as handle:
            self.hashtags = pickle.loads(handle.read())

        self.line_edit_clusters.setDisabled(False)
        self.button_clusterize.setDisabled(False)
        print(file_name)
        self.file_name = file_name[:-4].split("/tweets/")[1]

        self.line_edit_clusters.setDisabled(False)
        self.button_clusterize.setDisabled(False)

    def add_wordcloud_widget(self):
        """Add the wordcloud widget to the main layout in response of a click event."""
        
        self.clear_layout()
        tweets = [t[2] for t in self.tweets]
        widget_wordcloud = WidgetWordcloud(tweets, self.file_name, self.regenerate_wordcloud)
        self.vlayout_content.addWidget(widget_wordcloud)

        self.regenerate_wordcloud = False


    def add_wordcloud_per_cluster_widget(self):
        """Add the wordcloud per cluster widget to the main layout in response of a click event."""
        
        self.clear_layout()
        tweets = [t[2] for t in self.tweets]

        # Calculate from wich cluster each tweet belongs to
        tweets_per_cluster = {}
        for tweet, label in zip(tweets, self.labels):
            if label in tweets_per_cluster:
                tweets_per_cluster[label].append(tweet)
            else:
                tweets_per_cluster[label] = [tweet]

        widget_wordcloud_per_cluster = WidgetWordcloudPerCluster(tweets_per_cluster, self.file_name, 
                                                                 self.regenerate_wordcloud_per_cluster)
        self.vlayout_content.addWidget(widget_wordcloud_per_cluster)


    def clear_layout(self):
        """Remove all the widgets from the main layout."""
        while self.vlayout_content.count():
            child = self.vlayout_content.takeAt(0)
            child.widget().deleteLater()