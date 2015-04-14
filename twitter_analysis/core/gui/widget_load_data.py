# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import os.path
import os
import pickle

from core.gui.ui_widget_load_data import Ui_widget_load_dataset

class WidgetLoadData(QWidget, Ui_widget_load_dataset):
    """This widget loads the current clusterized dataset for analysis.
    
    Atributes
    ---------
    menu_analyse_tweets : QMenu
        Reference to the menu in the main window. It is enabled
        if a new dataset is loaded.
    """

    def __init__(self, menu_analyse_tweets):

        QWidget.__init__(self)
 
        self.menu_analyse_tweets = menu_analyse_tweets

        # set up User Interface (widgets, layout...)
        self.setupUi(self)
        self.lineEdit.setDisabled(True)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        if os.path.isfile(clusterized_dataset_path_file):
            
            with open(clusterized_dataset_path_file, 'rb') as handle:
                clusterized_dataset_path = pickle.loads(handle.read()) 
                self.lineEdit.setText(clusterized_dataset_path)

        # custom event handling
        self.button_open_file.clicked.connect(self.load_dataset_path)

    def load_dataset_path(self):
        """Load clusterized dataset path and save it for future analysis."""

        file_name = QtGui.QFileDialog.getOpenFileName(self, "Load filename", os.getcwd() + "\\tweets\\", "*.csv")
        self.lineEdit.setText(file_name)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl"
        if not os.path.isfile(clusterized_dataset_path_file):
            self.menu_analyse_tweets.setDisabled(False)
        else:
            with open(clusterized_dataset_path_file, 'rb') as handle:
                clusterized_dataset_path = pickle.loads(handle.read())

                if not clusterized_dataset_path == "":
                    self.menu_analyse_tweets.setDisabled(False)

        with open(clusterized_dataset_path_file, 'wb') as handle:
            pickle.dump(file_name, handle) 

        if file_name == "":
            self.menu_analyse_tweets.setDisabled(True)

        if not self.menu_analyse_tweets.isEnabled() and not file_name == "":
            self.menu_analyse_tweets.setDisabled(False)