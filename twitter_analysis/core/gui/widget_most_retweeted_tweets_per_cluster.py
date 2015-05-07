# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import csv
import os
import pickle

from core.gui.ui_widget_most_retweeted_tweets_per_cluster import Ui_widget_most_retweeted_tweets

class WidgetMostRetweetedTweetsPerCluster(QWidget, Ui_widget_most_retweeted_tweets):
    """This widget display the most retweeted tweets per cluster."""
    
    def __init__(self):

        QWidget.__init__(self)
 
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            clusterized_dataset_path = pickle.loads(handle.read())

        self.tweets = []
        with open(clusterized_dataset_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.tweets.append((tweet[0], tweet[2], tweet[3]))

        clusters = set([tweet[0] for tweet in self.tweets])

        self.combo_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(len(clusters))])
        self.combo_cluster.activated[int].connect(self.on_activated_combo_cluster)

    def on_activated_combo_cluster(self, cluster_label):

        tweets = [tweet for tweet in self.tweets if int(tweet[0]) == cluster_label]

        most_retweeted_tweets = sorted(tweets, key=lambda x:x[1])
        most_retweeted_tweets = most_retweeted_tweets[:-10:-1]

        self.text_edit_most_retweeted_tweets.setText("\n\n".join([tweet[2] for tweet in most_retweeted_tweets])) 
