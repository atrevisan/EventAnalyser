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

from core.gui.ui_widget_wordcloud_per_cluster import Ui_widget_wordcloud_per_cluster
from core.textutils.wordcloud import WordCloud

class WidgetWordcloudPerCluster(QWidget, Ui_widget_wordcloud_per_cluster):
    """This widget contains a label for displaying a wordcloud and a combobox for cluster choice.
    
    The wordcloud is generated based on a vectorizer that is used
    to calculate the importance of each word in the dataset.

    Parameters
    ----------
    file_name : string
        The base file name for the wordclouds that are being loaded
        from each cluster.

     k : int
        The number of clusters.
    """
    def __init__(self, file_name, k):

        QWidget.__init__(self)

        self.file_name = file_name
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.combobox_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(k)])
        self.combobox_cluster.activated[int].connect(self.onActivated)   

    def onActivated(self, cluster_label):

        wordcloud_file_name = os.getcwd() + "\\wordclouds\\" + self.file_name + "_cluster_" + str(cluster_label) + ".png"
 
        image = QtGui.QImage(wordcloud_file_name)
        pp = QtGui.QPixmap.fromImage(image)

        self.label_wordcloud.setPixmap(pp)