from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from Ui_WidgetAnalyseTweets import Ui_widgetAnalyseTweets
import os


class WidgetAnalyseTweets(QWidget, Ui_widgetAnalyseTweets):

    def __init__(self):

        QWidget.__init__(self)
     
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        twitterDataSetNames = [file for file in os.listdir("tweets/") if file.endswith(".csv")]

        self.comboBoxTweets.addItems(twitterDataSetNames)

        # custom event handling
        