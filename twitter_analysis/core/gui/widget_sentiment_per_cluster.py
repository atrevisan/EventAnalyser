# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import os
import csv
from PIL import Image
import pickle

from core.gui.ui_widget_sentiment_per_cluster import Ui_widget_sentiment_per_cluster
from core.textutils.text_analysis import PlotGenerator, TwitterDataAnalysis

class WidgetSentimentPerCluster(QWidget, Ui_widget_sentiment_per_cluster):
    """This widget contains a label for displaying a pie chart for the percentage of positive/negative sentiment for the chosen cluster.
    
    Atributes
    -------
    predicted_classes_per_cluster : list of tuples (float, float) 
       The first element is the percentage of positive sentiment documents
       and the second element is the percentage of negative sentiment documents.

    plot_generator : PlotGenerator
        Used to generate a plot of the percentage of positive/negative sentiment
        for the chosen cluster.

    clusterized_dataset_path : string
        The path to the clusterized tweets that will be analysed for extracting
        the percentage of positive/negative sentiment.
    """

    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf" 
        with open(sentiment_classification_model_path_file, 'rb') as handle:
            sentiment_classification_model_path = pickle.loads(handle.read())

        with open(sentiment_classification_model_path, 'rb') as handle:
            sentiment_classification_model = pickle.loads(handle.read())

        with open(sentiment_classification_model_path[:-14] + "feature_extractor.pkl", 'rb') as handle:
            sentiment_classification_feature_extractor = pickle.loads(handle.read())

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            self.clusterized_dataset_path = pickle.loads(handle.read())

        tweets = []
        with open(self.clusterized_dataset_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                tweets.append((tweet[0], tweet[1], tweet[2], tweet[3], tweet[4], tweet[5]))

        twitter_data_analyser = TwitterDataAnalysis(tweets)
        self.predicted_classes_per_cluster = twitter_data_analyser.generate_dataset_sentiment_info_per_cluster(sentiment_classification_feature_extractor, 
                                                                                                               sentiment_classification_model)
        
        self.plot_generator = PlotGenerator()

        number_of_clusters = len(set([tweet[0] for tweet in tweets]))
        self.combo_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(number_of_clusters)])
        self.combo_cluster.activated[int].connect(self.on_activated_combo_cluster)

    def on_activated_combo_cluster(self, cluster_label):

        pie_chart_file_name = self.clusterized_dataset_path[:-4] + "_cluster_" + str(cluster_label) + "_pie_chart.png"

        positive_sentiment_percentage, negative_sentiment_percentage = self.predicted_classes_per_cluster[cluster_label]
        self.plot_generator.create_pie_chart(pie_chart_file_name, [positive_sentiment_percentage, negative_sentiment_percentage])

        image = QtGui.QImage(pie_chart_file_name)
        pp = QtGui.QPixmap.fromImage(image)
        self.label_sentiment_percentage.setPixmap(pp)