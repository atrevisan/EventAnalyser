# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Nov 18 09:34:06 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from FetchTweets import Ui_fetchTweetsObject
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindowObject(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindowObject, self).__init__()
        
        self.setupUi(self)

    def setupUi(self, MainWindowObject):
        MainWindowObject.setObjectName(_fromUtf8("MainWindowObject"))
        MainWindowObject.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindowObject)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindowObject.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowObject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEvent_Analysis = QtGui.QMenu(self.menubar)
        self.menuEvent_Analysis.setObjectName(_fromUtf8("menuEvent_Analysis"))
        MainWindowObject.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowObject)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowObject.setStatusBar(self.statusbar)
        self.actionFetch_Tweets = QtGui.QAction(MainWindowObject)
        self.actionFetch_Tweets.setObjectName(_fromUtf8("actionFetch_Tweets"))
        self.actionAnalyse_Tweets = QtGui.QAction(MainWindowObject)
        self.actionAnalyse_Tweets.setObjectName(_fromUtf8("actionAnalyse_Tweets"))
        self.menuEvent_Analysis.addAction(self.actionFetch_Tweets)
        self.menuEvent_Analysis.addAction(self.actionAnalyse_Tweets)
        self.menubar.addAction(self.menuEvent_Analysis.menuAction())

        self.retranslateUi(MainWindowObject)
        QtCore.QMetaObject.connectSlotsByName(MainWindowObject)

        self.show()

    def retranslateUi(self, MainWindowObject):
        MainWindowObject.setWindowTitle(_translate("MainWindowObject", "Twitter Event Analyser", None))
        self.menuEvent_Analysis.setTitle(_translate("MainWindowObject", "Event Analysis", None))
        self.actionFetch_Tweets.setText(_translate("MainWindowObject", "Fetch Tweets", None))
        self.actionAnalyse_Tweets.setText(_translate("MainWindowObject", "Analyse Tweets", None))
        self.actionFetch_Tweets.triggered.connect(self.addFetchTweetsWidget)

    def addFetchTweetsWidget(self):
        print("oi")
        fetchTweetsWidget = Ui_fetchTweetsObject(self)
        self.setCentralWidget(fetchTweetsWidget)
        
        
        

def main():
    
    app = QtGui.QApplication(sys.argv)
    ui = Ui_MainWindowObject()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

