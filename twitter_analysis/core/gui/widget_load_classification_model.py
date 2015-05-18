# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import os.path
import os
import pickle

from core.gui.ui_widget_load_classification_model import Ui_widget_load_sentiment_classification_model

class WidgetLoadClassificationModel(QWidget, Ui_widget_load_sentiment_classification_model):
    """This widget loads the current active classification model that will be used for data analysis."""

    def __init__(self):

        QWidget.__init__(self)
 
        # set up User Interface (widgets, layout...)
        self.setupUi(self)
        self.lineEdit.setDisabled(True)

        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf" 
        if os.path.isfile(sentiment_classification_model_path_file):
            
            with open(sentiment_classification_model_path_file, 'rb') as handle:
                sentiment_classification_model_path = pickle.loads(handle.read()) 
                self.lineEdit.setText(sentiment_classification_model_path)

        # custom event handling
        self.button_open_file.clicked.connect(self.load_sentiment_classifier_path)

    def load_sentiment_classifier_path(self):
        """Load sentiment classifier path and save it for future analysis."""

        file_name = QtGui.QFileDialog.getOpenFileName(self, "Load filename", os.getcwd() + "\\sentiment_classification_models\\", "*.clf")
        self.lineEdit.setText(file_name)

        sentiment_classification_model_path_file = os.getcwd() + r"\core\gui\sentiment_classification_model_path.clf"

        with open(sentiment_classification_model_path_file, 'wb') as handle:
            pickle.dump(file_name, handle) 