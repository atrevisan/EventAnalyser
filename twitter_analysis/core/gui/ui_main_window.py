# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Jan 11 19:05:56 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(1120, 840)
        self.widget_central_widget = QtGui.QWidget(main_window)
        self.widget_central_widget.setObjectName(_fromUtf8("widget_central_widget"))
        main_window.setCentralWidget(self.widget_central_widget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_text_analysis = QtGui.QMenu(self.menubar)
        self.menu_text_analysis.setObjectName(_fromUtf8("menu_text_analysis"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        self.action_fetch_tweets = QtGui.QAction(main_window)
        self.action_fetch_tweets.setObjectName(_fromUtf8("action_fetch_tweets"))
        self.action_analyse_tweets = QtGui.QAction(main_window)
        self.action_analyse_tweets.setObjectName(_fromUtf8("action_analyse_tweets"))
        self.action_ml_config = QtGui.QAction(main_window)
        self.action_ml_config.setObjectName(_fromUtf8("action_ml_config"))
        self.action_text_analysis_config = QtGui.QAction(main_window)
        self.action_text_analysis_config.setObjectName(_fromUtf8("action_text_analysis_config"))
        self.menu_text_analysis.addAction(self.action_fetch_tweets)
        self.menu_text_analysis.addAction(self.action_analyse_tweets)
        self.menu_text_analysis.addAction(self.action_ml_config)
        self.menu_text_analysis.addAction(self.action_text_analysis_config)
        self.menubar.addAction(self.menu_text_analysis.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Twitter text analyser", None))
        self.menu_text_analysis.setTitle(_translate("main_window", "Text analysis", None))
        self.action_fetch_tweets.setText(_translate("main_window", "Fetch tweets", None))
        self.action_analyse_tweets.setText(_translate("main_window", "Analyse tweets", None))
        self.action_ml_config.setText(_translate("main_window", "ML config", None))
        self.action_text_analysis_config.setText(_translate("main_window", "Text analysis config", None))

