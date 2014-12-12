# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Nov 18 09:34:06 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_MainWindow import Ui_MainWindowObject
from WidgetFetchTweets import WidgetFetchTweets
from WidgetAnalyseTweets import WidgetAnalyseTweets

class MainWindow(QMainWindow, Ui_MainWindowObject):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # custom event handling
        self.actionFetch_Tweets.triggered.connect(self.addFetchTweetsWidget)
        self.actionAnalyse_Tweets.triggered.connect(self.addAnalyseTweetsWidget)

    def addFetchTweetsWidget(self):

        widgetFetchTweets = WidgetFetchTweets(self)
        self.setCentralWidget(widgetFetchTweets)

    def addAnalyseTweetsWidget(self):

        widgetAnalyseTweets = WidgetAnalyseTweets()
        self.setCentralWidget(widgetAnalyseTweets)

# Main entry to program.  Sets up the main app and create a new window.
def main(argv):
 
    # create Qt application
    app = QApplication(argv)
 
    # create main window
    wnd = MainWindow() # classname
    wnd.show()
 
    # Connect signal for app finish
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
 
    # Start the app up
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main(sys.argv)

