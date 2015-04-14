# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_analyse_tweets.ui'
#
# Created: Wed Apr  1 08:49:35 2015
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

class Ui_widget_analyse_tweets(object):
    def setupUi(self, widget_analyse_tweets):
        widget_analyse_tweets.setObjectName(_fromUtf8("widget_analyse_tweets"))
        widget_analyse_tweets.resize(800, 600)
        self.horizontalLayout = QtGui.QHBoxLayout(widget_analyse_tweets)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_main_widget = QtGui.QWidget(widget_analyse_tweets)
        self.widget_main_widget.setStyleSheet(_fromUtf8("QWidget#widget_main_widget { \n"
"\n"
"     border: 2px solid gray; \n"
"  \n"
" } "))
        self.widget_main_widget.setObjectName(_fromUtf8("widget_main_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_main_widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vlayout_content = QtGui.QVBoxLayout()
        self.vlayout_content.setObjectName(_fromUtf8("vlayout_content"))
        self.horizontalLayout_2.addLayout(self.vlayout_content)
        self.horizontalLayout.addWidget(self.widget_main_widget)

        self.retranslateUi(widget_analyse_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_analyse_tweets)

    def retranslateUi(self, widget_analyse_tweets):
        widget_analyse_tweets.setWindowTitle(_translate("widget_analyse_tweets", "Analyse Tweets", None))

