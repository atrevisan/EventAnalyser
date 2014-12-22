# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QMainWindow
from gui.ui_main_window import Ui_main_window
from gui.widget_fetch_tweets import WidgetFetchTweets

class MainWindow(QMainWindow, Ui_main_window):
    """The application main window."""

    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # custom event handling
        self.action_fetch_tweets.triggered.connect(self.add_widget_fetch_tweets)
        self.action_analyse_tweets.triggered.connect(self.add_widget_analyse_tweets)

    def add_widget_fetch_tweets(self):
        
        widgetFetchTweets = WidgetFetchTweets(self)
        self.setCentralWidget(widgetFetchTweets)

    def add_widget_analyse_tweets(self):
        pass
        #widgetAnalyseTweets = WidgetAnalyseTweets()
        #self.setCentralWidget(widgetAnalyseTweets)


