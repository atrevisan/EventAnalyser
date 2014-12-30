# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

from core.gui.ui_widget_analyse_tweets import Ui_widget_analyse_tweets
from core.gui.widget_wordcloud import WidgetWordcloud

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
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # for some reason not loading icons correctly inside designer
        self.button_open_file.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\open.png")))

        # custom event handling
        self.button_open_file.clicked.connect(self.open_tweets_file)
        self.button_wordcloud.clicked.connect(self.add_wordcloud_widget)

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

    def add_wordcloud_widget(self):
        """Add the wordcloud widget to the main layout in response of a click event."""
        
        self.clear_layout()
        tweets = [t[2] for t in self.tweets]
        widget_wordcloud = WidgetWordcloud(tweets)
        self.vlayout_content.addWidget(widget_wordcloud)

    def clear_layout(self):
        """Remove all the widgets from the main layout."""
        while self.vlayout_content.count():
            child = self.vlayout_content.takeAt(0)
            child.widget().deleteLater()