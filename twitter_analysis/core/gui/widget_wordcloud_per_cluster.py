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
    tweets_per_cluster : dict of lists of strings
        The list of words that will be used in the wordcloud is obtained
        from this dataset. Mappings from cluster label to list of documents.

    file_name : string
        The file name for the wordcloud that is being generated.

     regenerate_files : list
        Contains file names that need to be regenarated in case a new dataset is selected.
    """
    def __init__(self, tweets_per_cluster, file_name, regenerate_files):

        QWidget.__init__(self)

        self.tweets_per_cluster = tweets_per_cluster
        self.file_name = file_name
        self.regenerate_files = regenerate_files
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.combobox_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(len(tweets_per_cluster))])
        self.combobox_cluster.activated[int].connect(self.onActivated)   

    def onActivated(self, cluster_label):

        filename = os.getcwd() + "\\wordclouds\\" + self.file_name + "_cluster_" + str(cluster_label) + ".png"
        
        if not filename in self.regenerate_files:

            wordcloud = WordCloud(max_words=20, prefer_horizontal=0.80).generate(raw_documents=self.tweets_per_cluster[cluster_label])
            wordcloud.to_file(filename)

            image = QtGui.QImage(filename)
            pp = QtGui.QPixmap.fromImage(image)

            self.label_wordcloud.setPixmap(pp)

            self.regenerate_files.append(filename)

        else:

            image = QtGui.QImage(filename)
            pp = QtGui.QPixmap.fromImage(image)

            self.label_wordcloud.setPixmap(pp)
        