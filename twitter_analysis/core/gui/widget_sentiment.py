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

from core.gui.ui_widget_sentiment import Ui_widget_sentiment
from core.textutils.text_analysis import PlotGenerator, TwitterDataAnalysis

class WidgetSentiment(QWidget, Ui_widget_sentiment):
    """This widget contains a label for displaying a pie chart for the percentage of positive/negative sentiment."""

    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf" 
        with open(sentiment_classification_model_path_file, 'rb') as handle:
            sentiment_classification_model_path = pickle.loads(handle.read())

        with open(sentiment_classification_model_path, 'rb') as handle:
            sentiment_classification_model = pickle.loads(handle.read())

        with open(sentiment_classification_model_path[:-14] + "vectorizer.pkl", 'rb') as handle:
            sentiment_classification_vectorizer = pickle.loads(handle.read())

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            clusterized_dataset_path = pickle.loads(handle.read())

        tweets = []
        with open(clusterized_dataset_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                tweets.append((tweet[0], tweet[1], tweet[2], tweet[3], tweet[4], tweet[5]))

        twitter_data_analyser = TwitterDataAnalysis(tweets)
        positive_sentiment_percentage, negative_sentiment_percentage =  twitter_data_analyser.generate_dataset_sentiment_info(sentiment_classification_vectorizer, sentiment_classification_model)

        plot_generator = PlotGenerator()

        pie_chart_file_name = clusterized_dataset_path[:-4] + "_pie_chart.png"
        plot_generator.create_pie_chart(pie_chart_file_name, [positive_sentiment_percentage, negative_sentiment_percentage])

        image = QtGui.QImage(pie_chart_file_name)
        pp = QtGui.QPixmap.fromImage(image)
        self.label_sentiment_percentage.setPixmap(pp)