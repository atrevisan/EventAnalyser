# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QMainWindow
import os.path
import pickle

from core.gui.ui_main_window import Ui_main_window
from core.gui.widget_fetch_tweets import WidgetFetchTweets
from core.gui.widget_analyse_tweets import WidgetAnalyseTweets
from core.gui.widget_clustering_config import WidgetClusteringConfig
from core.gui.widget_load_data import WidgetLoadData
from core.gui.widget_wordcloud import WidgetWordcloud
from core.gui.widget_wordcloud_per_cluster import WidgetWordcloudPerCluster

class MainWindow(QMainWindow, Ui_main_window):
    """The application main window."""

    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.menu_analyse_tweets.setDisabled(True)

        clusterized_dataset_path_file = os.getcwd() + r"\core\gui\clusterized_dataset_path.pkl" 
        if os.path.isfile(clusterized_dataset_path_file):
            with open(clusterized_dataset_path_file, 'rb') as handle:
                clusterized_dataset_path = pickle.loads(handle.read())

                if not clusterized_dataset_path == "":
                    self.menu_analyse_tweets.setDisabled(False)

        # custom event handling
        self.action_fetch_tweets.triggered.connect(self.add_widget_fetch_tweets)
        self.action_clustering_config.triggered.connect(self.add_widget_clustering_config)
        self.action_load_dataset.triggered.connect(self.add_widget_load_dataset)
        self.action_wordcloud.triggered.connect(self.add_widget_wordcloud)
        self.action_wordcloud_per_cluster.triggered.connect(self.add_widget_wordcloud_per_cluster)
        

    def add_widget_clustering_config(self):
        """Replace the current widget for a new widget widget_clustering_config.
        
        This widget displays gui elements for dealing with the configuration 
        of the tweets clustering procedure.
        """

        widget_clustering_config = WidgetClusteringConfig()
        self.setCentralWidget(widget_clustering_config)
        
    def add_widget_fetch_tweets(self):
        """Replaces the current widget for a new widget_fetch_tweets.
        
        This widget has gui elements for making Twitter querries and
        save querry results to a csv file.
        """

        widget_fetch_tweets = WidgetFetchTweets()
        self.setCentralWidget(widget_fetch_tweets)

    def add_widget_analyse_tweets(self):
        """Replaces the current widget for a new analyse tweets widget.
        
        The analyse tweets widget contains gui elements for making text analysis
        over Twitter text data.
        """
       
        widget_analyse_tweets = WidgetAnalyseTweets()
        self.setCentralWidget(widget_analyse_tweets)

    def add_widget_load_dataset(self):
        """Replaces the current widget for a new widget_load_data.
        
        This widget has gui elements for loading the clusterized
        dataset path.

        Note
        ----
        The tweets text analysis menu items are enabled only if
        there is some clusterized dataset path loaded.
        """
       
        widget_load_data = WidgetLoadData(self.menu_analyse_tweets)
        self.setCentralWidget(widget_load_data)

    def add_widget_wordcloud(self):
        """Replaces the current widget for a new widget_wordcloud.
        
        This widget displays a wordcloud for the top ngrams in
        the dataset.
        """

        widget_wordcloud = WidgetWordcloud()
        self.setCentralWidget(widget_wordcloud)

    def add_widget_wordcloud_per_cluster(self):
        """Replaces the current widget for a new widget_wordcloud_per_cluster.
        
        This widget displays a wordcloud for the top ngrams in
        the chosen dataset cluster.
        """

        widget_wordcloud_per_cluster = WidgetWordcloudPerCluster()
        self.setCentralWidget(widget_wordcloud_per_cluster)