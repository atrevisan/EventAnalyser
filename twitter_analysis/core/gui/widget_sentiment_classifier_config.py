# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCursor
from PyQt4.QtGui import QMessageBox

import os
import numpy as np
import csv
import pickle
import itertools
                 
from core.gui.ui_widget_sentiment_classifier_config import Ui_widget_sentiment_classifier_config                        
from core.textutils.feature_extraction import FeatureExtractor
from core.ml.document_classification import DocumentClassification


class WidgetSentimentClassifierConfig(QWidget, Ui_widget_sentiment_classifier_config):
    """This widget displays a range of options for text classification alghorithms,
   namely Suport Vector Machines and Nave Bayes.

    Atributes
    -------
    training_data : array[n_samples, n_features]
        Vectorized training data obtained from the feature extraction process.

    training_labels : list[n_samples]
        Target values for the training data.

    test_data : array[n_samples, n_features]
        Vectorized test data obtained from the feature extraction process.

    test_labels : list[n_samples]
        Target values for the test data.

    fe : FeatureExtractor
        Handles the conversion of a corpus of raw text documents to a matrix of numeric
        features.

    dc : DocumentClassification
        Handles the fit of a classification model to a vectorized labeled corpus of
        text documents.
    """
    def __init__(self):

        QWidget.__init__(self)

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.positive_sentiment_dataset = []
        self.negative_sentiment_dataset = []

        self.groupBox.setDisabled(True)
        self.groupBox_2.setDisabled(True)

        root_directory = os.getcwd()
        root_directory = root_directory.replace("\\", "/")

        stylesheet = """QPushButton#button_save_sentiment_classifier_config {
            
                            background-color: transparent;
                            background-image: url('%s/core/gui/assets/save.png');
                            background-repeat: no-repeat;
                        }
        
                        QPushButton#button_save_sentiment_classifier_config:hover {
                            background-color: transparent;
                            background-image: url('%s/core/gui/assets/save_2.png');
                            background-repeat: no-repeat;
                        }
            
                        QPushButton#button_save_sentiment_classifier_config:pressed {
                            background-color: transparent;
                            background-image: url('%s/core/gui/assets/save.png');
                            background-repeat: no-repeat;
                        }
        """ %(root_directory, root_directory, root_directory)

        self.button_save_sentiment_classifier_config.setStyleSheet(stylesheet)
        
        self.combo_vectorizer.addItems(["tfidf vectorizer", "count vectorizer"])
        self.combo_ngram_range.addItems(["(1,1)", "(1,2)", "(1,3)", "(2,2)", "(2,3)", "(3,3)"])
        self.combo_max_df.addItems(["%.1f" % number for number in list(np.arange(0.0, 1.1, 0.1))] + [str(number) for number in list(range(1, 10001))]) 
        self.combo_min_df.addItems(["%.1f" % number for number in list(np.arange(0.0, 1.1, 0.1))] + [str(number) for number in list(range(1, 10001))])
        self.combo_max_features.addItems([str(num) for num in list(range(2, 10001))])
        self.combo_num_of_components.addItems([str(num) for num in list(range(2, 500))])
        self.combo_classifier.addItems(["Multinomial NB", "Linear SVC"])
        self.combo_regularization.addItems(["%.1f" % number for number in list(np.arange(0.0, 1.1, 0.1))])

        self.combo_ngram_range.setCurrentIndex(1)
        self.combo_max_df.setCurrentIndex(5)
        self.combo_min_df.setCurrentIndex(1)
        self.combo_max_features.setCurrentIndex(498)
        self.combo_num_of_components.setCurrentIndex(98)
        self.combo_classifier.setCurrentIndex(0)
        self.combo_regularization.setCurrentIndex(5)

        self.check_use_idf.setChecked(True)
        self.check_remove_stopwords.setChecked(True)
        self.combo_num_of_components.setDisabled(True)
        self.combo_regularization.setDisabled(True)

        self.combo_vectorizer.activated[str].connect(self.on_activated_combo_vectorizer)
        self.combo_max_features.activated[int].connect(self.on_activated_combo_max_features)
        self.combo_classifier.activated[str].connect(self.on_activated_combo_classifier)

        self.check_perform_lsa.stateChanged.connect(self.check_lsa_state_changed)
        self.button_train.clicked.connect(self.train_sentiment_classifier)
        self.button_vectorize.clicked.connect(self.vectorize_data)
        self.button_open_positive_sentiment_dataset.clicked.connect(self.open_positive_sentiment_dataset)
        self.button_open_negative_sentiment_dataset.clicked.connect(self.open_negative_sentiment_dataset)
        self.button_save_sentiment_classifier_config.clicked.connect(self.save_classification_model)
     
    def open_positive_sentiment_dataset(self):
        """Load positive class data for training a classifier."""
            
        # user chosen file 
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open data", os.getcwd() + "\\tweets\\", "*.csv")
 
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.positive_sentiment_dataset.append(tweet[2])

        if self.negative_sentiment_dataset:
            self.groupBox.setDisabled(False)
            self.groupBox_2.setDisabled(False)

    def open_negative_sentiment_dataset(self):
        """Load negative class data for training a classifier."""
            
        # user chosen file 
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open data", os.getcwd() + "\\tweets\\", "*.csv")
 
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.negative_sentiment_dataset.append(tweet[2])

        if self.positive_sentiment_dataset:
            self.groupBox.setDisabled(False)
            self.groupBox_2.setDisabled(False)
        

    def vectorize_data(self):
        """Perform trainning data vecorization."""
        
        # vectorization parameters
        vectorizer = self.combo_vectorizer.currentText()
        ngram_range = [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)][self.combo_ngram_range.currentIndex()]
        max_df = list(itertools.chain([number for number in list(np.arange(0.0, 1.1, 0.1))], list(range(1, 10001))))[self.combo_max_df.currentIndex()]
        min_df = list(itertools.chain([number for number in list(np.arange(0.0, 1.1, 0.1))], list(range(1, 10001))))[self.combo_min_df.currentIndex()]
        max_features = list(range(2, 10001))[self.combo_max_features.currentIndex()]
        use_idf = not self.check_use_idf is None and self.check_use_idf.isChecked()
        use_stemming = self.check_use_stemming.isChecked()
        binary = self.check_binary.isChecked()
        remove_stopwords = self.check_remove_stopwords.isChecked()
        
        # balancing positive/negative class dataset size
        if len(self.positive_sentiment_dataset) > len(self.negative_sentiment_dataset):
            self.positive_sentiment_dataset = self.positive_sentiment_dataset[:len(self.negative_sentiment_dataset)]
        elif len(self.negative_sentiment_dataset) > len(self.positive_sentiment_dataset):
            self.negative_sentiment_dataset = self.negative_sentiment_dataset[:len(self.positive_sentiment_dataset)]

        # separate dataset in training and testing
        cutoff = int(0.8 * len(self.positive_sentiment_dataset))
        
        training_data = self.positive_sentiment_dataset[:cutoff] + self.negative_sentiment_dataset[:cutoff]
        self.training_labels = [0 for i in range(len(self.positive_sentiment_dataset[:cutoff]))] + [1 for i in range(len(self.negative_sentiment_dataset[:cutoff]))]

        test_data = self.positive_sentiment_dataset[cutoff:] + self.negative_sentiment_dataset[cutoff:]
        self.test_labels = [0 for i in range(len(self.positive_sentiment_dataset[cutoff:]))] + [1 for i in range(len(self.negative_sentiment_dataset[cutoff:]))]

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        self.fe = FeatureExtractor(training_data, 
                                   max_df=max_df, 
                                   min_df=min_df,
                                   max_features=max_features, 
                                   ngram_range=ngram_range, 
                                   use_stemming=use_stemming,
                                   binary=binary,
                                   remove_stopwords=remove_stopwords) 

        try:
            if vectorizer == "tfidf vectorizer":

                self.fe.tfidf_vectorizer(use_idf=use_idf)

            else:
                self.fe.count_vectorizer()

            self.training_data = self.fe.X
            self.test_data = self.fe.vectorizer.transform(test_data)
            
            n_features = self.fe.X.shape[1]
            self.label_features.setText(str(n_features))

        except ValueError:
            QMessageBox.about(self, "Error", "Problem while extracting features")

        QApplication.restoreOverrideCursor()

    def train_sentiment_classifier(self):
        """Perform the classification procedure."""
        
        perform_lsa = self.check_perform_lsa.isChecked()
        max_features = list(range(2, 10001))[self.combo_max_features.currentIndex()]
        n_components = list(range(2, max_features + 1))[self.combo_num_of_components.currentIndex()]

        classification_method = self.combo_classifier.currentText()

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        self.dc = DocumentClassification(self.training_data, self.training_labels, self.test_data, self.test_labels, perform_lsa=perform_lsa, n_components=n_components)

        if classification_method == "Multinomial NB":
            self.dc.multinomialNB()
        else:
            C = float(self.combo_regularization.currentText())
            self.dc.linearSVC(C=C)

        classification_time = self.dc.classification_time
        self.label_classification_time.setText(classification_time)
            
        if perform_lsa:
            self.label_explained_variance.setText(str(self.dc.explained_variance) + "%")
       
        QApplication.restoreOverrideCursor()
    
    def save_object(self, obj, filename):
        """Save objet to file.
        
        Parameters
        -----------
        obj : some object
           Object that will be saved.

        filename : str
            Filesystem path to wich the object should
            be saved.
        """
        with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    def save_classification_model(self):
        """Save the obtained classification model.
        
        Save the classification object that will be used in
        the tweets text analysis module. Save also the vectorizer
        used to obtain the features used in the classifier so that
        unseen data can be vectorized.
        """

        file_name = QtGui.QFileDialog.getSaveFileName(self, "Save model", os.getcwd() + "\\sentiment_classification_models\\", "*.csv")

        # Case the user select an already existent file
        if file_name.find(".pkl") != -1:
            file_name = file_name[:-4]

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        self.save_object(self.fe.vectorizer, file_name + "_vectorizer.pkl")
        self.save_object(self.dc, file_name + "_classifier.pkl")

        QApplication.restoreOverrideCursor()

    def on_activated_combo_vectorizer(self, vectorizer):

        if vectorizer == "count vectorizer" and not self.check_use_idf is None:
        
            self.vlayout_checkboxes.removeWidget(self.check_use_idf)
            self.check_use_idf.deleteLater()
            self.check_use_idf = None

        elif vectorizer == "tfidf vectorizer" and self.check_use_idf is None:
            
            self.check_use_idf = QtGui.QCheckBox()
            font = QtGui.QFont()
            font.setPointSize(10)
            self.check_use_idf.setFont(font)
            self.check_use_idf.setObjectName("check_use_idf")
            self.vlayout_checkboxes.addWidget(self.check_use_idf)
            self.check_use_idf.setText("use idf")

    def on_activated_combo_max_features(self, index):

        self.combo_num_of_components.clear()
        self.combo_num_of_components.addItems([str(num) for num in list(range(2, list(range(2, 10001))[index]))])

    def check_lsa_state_changed(self, state):

        if state == QtCore.Qt.Checked:
            self.combo_num_of_components.setDisabled(False)
        else:
            self.combo_num_of_components.setDisabled(True)

    def on_activated_combo_classifier(self, classifier):

        if classifier == "Multinomial NB":

            self.combo_regularization.setDisabled(True)
        else:
            self.combo_regularization.setDisabled(False)
