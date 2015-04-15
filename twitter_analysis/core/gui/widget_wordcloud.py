# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import os

import PIL
from PIL import Image
import pickle

from core.gui.ui_widget_wordcloud import Ui_widget_wordcloud
from core.textutils.wordcloud import WordCloud

class WidgetWordcloud(QWidget, Ui_widget_wordcloud):
    """This widget contains a label for displaying a wordcloud.
    
    Notes
    -------
    The wordcloud is generated based on a vectorizer that is used
    to calculate the importance of each word in the dataset.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            clusterized_dataset_path = pickle.loads(handle.read())

        wordcloud_file_name = clusterized_dataset_path[:-4] + "_wordcloud.png"
        
        image = QtGui.QImage(wordcloud_file_name)
        pp = QtGui.QPixmap.fromImage(image)

        self.label_wordcloud.setPixmap(pp)