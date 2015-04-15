# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

import os
import os.path

import PIL
from PIL import Image
import pickle

from core.gui.ui_widget_wordcloud_per_cluster import Ui_widget_wordcloud_per_cluster
from core.textutils.wordcloud import WordCloud

class WidgetWordcloudPerCluster(QWidget, Ui_widget_wordcloud_per_cluster):
    """This widget contains a label for displaying a wordcloud and a combobox for cluster choice.
    
    The wordcloud is generated based on a vectorizer that is used
    to calculate the importance of each word in the dataset.
    """
    def __init__(self):

        QWidget.__init__(self)

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        with open(clusterized_dataset_path_file, 'rb') as handle:
            self.clusterized_dataset_path = pickle.loads(handle.read())

        with open(self.clusterized_dataset_path[:-4] + "_top_ngrams_per_cluster.pkl", 'rb') as handle:
            top_ngrams_per_cluster = pickle.loads(handle.read())

        self.combobox_cluster.addItems(["Cluster %d" % cluster_label for cluster_label in range(len(top_ngrams_per_cluster))])
        self.combobox_cluster.activated[int].connect(self.onActivated)   

    def onActivated(self, cluster_label):

        wordcloud_file_name = self.clusterized_dataset_path[:-4] + "_wordcloud_cluster_" + str(cluster_label) + ".png"
 
        image = QtGui.QImage(wordcloud_file_name)
        pp = QtGui.QPixmap.fromImage(image)

        self.label_wordcloud.setPixmap(pp)