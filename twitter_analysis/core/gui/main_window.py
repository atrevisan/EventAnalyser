# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QMainWindow
from core.gui.ui_main_window import Ui_main_window
from core.gui.widget_fetch_tweets import WidgetFetchTweets
from core.gui.widget_analyse_tweets import WidgetAnalyseTweets
from core.gui.widget_ml_config import WidgetMLConfig

class MainWindow(QMainWindow, Ui_main_window):
    """The application main window."""

    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # custom event handling
        self.action_fetch_tweets.triggered.connect(self.add_widget_fetch_tweets)
        self.action_analyse_tweets.triggered.connect(self.add_widget_analyse_tweets)
        self.action_ml_config.triggered.connect(self.add_widget_ml_config)

    def add_widget_ml_config(self):
        """Replace the current widget for a new ml config widget.
        
        The machine learning config widget display gui elements for
        dealing with the configuration of the clustering and 
        sentiment classification procedures.
        """

        widget_ml_config = WidgetMLConfig()
        self.setCentralWidget(widget_ml_config)
        
    def add_widget_fetch_tweets(self):
        """Replaces the current widget for a new fetch tweets widget.
        
        The fetch tweets widget contain gui elements for making Twitter searches.
        """

        widget_fetch_tweets = WidgetFetchTweets(self)
        self.setCentralWidget(widget_fetch_tweets)

    def add_widget_analyse_tweets(self):
        """Replaces the current widget for a new analyse tweets widget.
        
        The analyse tweets widget contains gui elements for making text analysis
        over Twitter text data.
        """
       
        widget_analyse_tweets = WidgetAnalyseTweets()
        self.setCentralWidget(widget_analyse_tweets)