# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QMainWindow
import os.path
import pickle

from core.gui.ui_main_window import Ui_main_window
from core.gui.widget_fetch_tweets import WidgetFetchTweets
from core.gui.widget_clustering_config import WidgetClusteringConfig
from core.gui.widget_sentiment_classifier_config import WidgetSentimentClassifierConfig
from core.gui.widget_load_data import WidgetLoadData
from core.gui.widget_load_classification_model import WidgetLoadClassificationModel
from core.gui.widget_wordcloud import WidgetWordcloud
from core.gui.widget_wordcloud_per_cluster import WidgetWordcloudPerCluster
from core.gui.widget_cosine_similarity import WidgetCosineSimilarity
from core.gui.widget_most_retweeted_tweets import WidgetMostRetweetedTweets
from core.gui.widget_most_retweeted_tweets_per_cluster import WidgetMostRetweetedTweetsPerCluster
from core.gui.widget_sentiment import WidgetSentiment
from core.gui.widget_sentiment_per_cluster import WidgetSentimentPerCluster
from core.gui.widget_ngrams import WidgetNGrams
from core.gui.widget_ngrams_per_cluster import WidgetNGramsPerCluster


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
        self.action_sentiment_classifier_config.triggered.connect(self.add_widget_sentiment_classifier_config)
        self.action_load_dataset.triggered.connect(self.add_widget_load_dataset)
        self.actionLoad_sentiment_classification_model.triggered.connect(self.add_widget_load_sentiment_classification_model)
        self.action_wordcloud.triggered.connect(self.add_widget_wordcloud)
        self.action_wordcloud_per_cluster.triggered.connect(self.add_widget_wordcloud_per_cluster)
        self.action_cosine_similarity.triggered.connect(self.add_widget_cosine_similarity)
        self.action_relevant_tweets.triggered.connect(self.add_widget_most_retweeted_tweets)
        self.action_relevant_tweets_per_cluster.triggered.connect(self.add_widget_most_retweeted_tweets_per_cluster)
        self.action_sentiment.triggered.connect(self.add_widget_sentiment)
        self.action_sentiment_per_cluster.triggered.connect(self.add_widget_sentiment_per_cluster)
        self.action_ngrams.triggered.connect(self.add_widget_ngrams)
        self.action_ngrams_per_cluster.triggered.connect(self.add_widget_ngrams_per_cluster)


    def add_widget_ngrams(self):
        """Replace the current widget for a new widget_ngrams.
        
        This widget displays statistical info regarding the
        dataset top ngrams.
        """

        widget_ngrams = WidgetNGrams()
        self.setCentralWidget(widget_ngrams)

    def add_widget_ngrams_per_cluster(self):
        """Replace the current widget for a new widget_ngrams_per_cluster.
        
        This widget displays statistical info regarding the
        dataset top ngrams per cluster.
        """

        widget_ngrams_per_cluster = WidgetNGramsPerCluster()
        self.setCentralWidget(widget_ngrams_per_cluster)

    def add_widget_clustering_config(self):
        """Replace the current widget for a new widget widget_clustering_config.
        
        This widget displays gui elements for dealing with the configuration 
        of the tweets clustering procedure.
        """

        widget_clustering_config = WidgetClusteringConfig()
        self.setCentralWidget(widget_clustering_config)

    def add_widget_sentiment_classifier_config(self):
        """Replace the current widget for a new widget widget_sentiment_classifier_config.
        
        This widget displays gui elements for dealing with the configuration 
        of the tweets sentiment classification procedure.
        """

        widget_sentiment_classification_config = WidgetSentimentClassifierConfig()
        self.setCentralWidget(widget_sentiment_classification_config)
        
    def add_widget_fetch_tweets(self):
        """Replaces the current widget for a new widget_fetch_tweets.
        
        This widget has gui elements for making Twitter querries and
        save querry results to a csv file.
        """

        widget_fetch_tweets = WidgetFetchTweets()
        self.setCentralWidget(widget_fetch_tweets)
        
    def add_widget_sentiment(self):
        """Replaces the current widget for a new widget_sentiment.
        
        This widget has gui elements for displaying the percentage of
        positive/negative sentiment overt a tweets dataset.
        """

        widget_sentiment = WidgetSentiment()
        self.setCentralWidget(widget_sentiment)

    def add_widget_sentiment_per_cluster(self):
        """Replaces the current widget for a new widget_sentiment_per_cluster.
        
        This widget has gui elements for displaying the percentage of
        positive/negative sentiment over a chosen cluster of tweets.
        """

        widget_sentiment_per_cluster = WidgetSentimentPerCluster()
        self.setCentralWidget(widget_sentiment_per_cluster)

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

    def add_widget_load_sentiment_classification_model(self):
        """Replaces the current widget for a new widget_load_sentiment_classification_model.
        
        This widget has gui elements for loading the sentiment classification model
        path.
        """

        widget_load_sentiment_classification_model = WidgetLoadClassificationModel()
        self.setCentralWidget(widget_load_sentiment_classification_model)

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

    def add_widget_cosine_similarity(self):
        """Replaces the current widget for a new widget_cosine_similarity.
        
        This widget makes possible for the user to search in the dataset
        for the tweets that resamble the most the suplied query.
        """

        widget_cosine_similarity = WidgetCosineSimilarity()
        self.setCentralWidget(widget_cosine_similarity)

    def add_widget_most_retweeted_tweets(self):
        """Replaces the current widget for a new widget_most_retweeted_tweets.
        
        This widget ranks the top most retweeted tweets in descending order of
        importance.
        """

        widget_most_retweet_tweets = WidgetMostRetweetedTweets()
        self.setCentralWidget(widget_most_retweet_tweets)

    def add_widget_most_retweeted_tweets_per_cluster(self):
        """Replaces the current widget for a new widget_most_retweeted_tweets_per_cluster.
        
        This widget ranks the top most retweeted tweets in the chosen cluster in descending order of
        importance.
        """

        widget_most_retweet_tweets_per_cluster = WidgetMostRetweetedTweetsPerCluster()
        self.setCentralWidget(widget_most_retweet_tweets_per_cluster)