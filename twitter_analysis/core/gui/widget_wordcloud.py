# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import os
from time import time

import PIL
from PIL import Image

from core.gui.ui_widget_wordcloud import Ui_widget_wordcloud
from core.textutils.wordcloud import WordCloud

class WidgetWordcloud(QWidget, Ui_widget_wordcloud):
    """This widget contains a label for displaying a wordcloud.
    
    Notes
    -------
    The wordcloud is generated based on a vectorizer that is used
    to calculate the importance of each word in the dataset.

    Parameters
    ----------
    file_name : string
        The base file name for the wordcloud that is being loaded.
    """
    def __init__(self, file_name):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        wordcloud_file_name = os.getcwd() + "\\wordclouds\\" + file_name + ".png"
        
        image = QtGui.QImage(wordcloud_file_name)
        pp = QtGui.QPixmap.fromImage(image)

        self.label_wordcloud.setPixmap(pp)