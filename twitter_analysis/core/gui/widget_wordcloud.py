# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import os
import os.path
from time import time

import PIL
from PIL import Image

from core.gui.ui_widget_wordcloud import Ui_widget_wordcloud
from core.textutils.wordcloud import WordCloud

class WidgetWordcloud(QWidget, Ui_widget_wordcloud):
    """This widget contains a label for displaying a wordcloud.
    
    The wordcloud is generated based on a vectorizer that is used
    to calculate the importance of each word in the dataset.

    Parameters
    ----------
    tweets : list of strings
        The list of words that will be used in the wordcloud is obtained
        from this dataset.

    file_name : string
        The file name for the wordcloud that is being generated.
    """
    def __init__(self, tweets, file_name):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        filename = os.getcwd() + "\\wordclouds\\" + file_name + ".png"
        
        if not os.path.isfile(filename): 
        
            wordcloud = WordCloud(max_words=30, prefer_horizontal=0.80).generate(raw_documents=tweets)
            wordcloud.to_file(filename)

        image = QtGui.QImage(filename)
        pp = QtGui.QPixmap.fromImage(image)

        self.label_wordcloud.setPixmap(pp)