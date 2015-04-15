# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import csv
import os
import pickle

from core.gui.ui_widget_cosine_similarity import Ui_widget_cosine_similarity
from core.textutils.feature_extraction import FeatureExtractor

class WidgetCosineSimilarity(QWidget, Ui_widget_cosine_similarity):
    """This widget search for the top tweets that resamble the most a search querry using cosine similarity measure."""
    def __init__(self):

        QWidget.__init__(self)
 
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        root_directory = os.getcwd()
        root_directory = root_directory.replace("\\", "/")

        stylesheet = """QPushButton#button_fetch_tweets {

	                        background-color: rgb(255, 255, 127);
	                        border-radius: 7px; 
	                        border: 2px solid gray;
                            background-image: url('%s/core/gui/assets/mg2.png');
                            background-repeat: no-repeat; 
                            background-position: center;
                    }

                    QPushButton#button_fetch_tweets:hover {
	                        background-color: rgb(227, 255, 82);
	                        border-style: inset;

                    }
 
                    QPushButton#button_fetch_tweets:pressed {
	                        background-color: rgb(255, 255, 127);
	                        border-style: inset;
                    }
                    """%root_directory

        self.button_fetch_tweets.setStyleSheet(stylesheet)

        # custom event handling
        self.button_fetch_tweets.clicked.connect(self.fetch_tweets)
        
    def fetch_tweets(self):
        """Search the dataset for the most similar documents to some search querry."""

        search_query = self.line_edit_querry.text()

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            clusterized_dataset_path = pickle.loads(handle.read())

        tweets = []
        tweets.append(search_query)

        with open(clusterized_dataset_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                tweets.append(tweet[3])

        fe = FeatureExtractor(tweets)
        fe.tfidf_vectorizer()
        
        top_documents = fe.get_top_documents_by_cosine_similarity()

        self.text_edit_most_relevant_tweets.setText("\n\n".join(top_documents))