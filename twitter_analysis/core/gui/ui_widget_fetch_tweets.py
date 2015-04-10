# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_fetch_tweets.ui'
#
# Created: Wed Apr  1 11:10:55 2015
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

class Ui_widget_fetch_tweets(object):
    def setupUi(self, widget_fetch_tweets):
        widget_fetch_tweets.setObjectName(_fromUtf8("widget_fetch_tweets"))
        widget_fetch_tweets.resize(800, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(widget_fetch_tweets.sizePolicy().hasHeightForWidth())
        widget_fetch_tweets.setSizePolicy(sizePolicy)
        widget_fetch_tweets.setStatusTip(_fromUtf8(""))
        widget_fetch_tweets.setWhatsThis(_fromUtf8(""))
        self.widget_querry_container = QtGui.QWidget(widget_fetch_tweets)
        self.widget_querry_container.setGeometry(QtCore.QRect(20, 20, 541, 41))
        self.widget_querry_container.setMaximumSize(QtCore.QSize(16777215, 51))
        self.widget_querry_container.setStyleSheet(_fromUtf8("\n"
"\n"
"QWidget#widget_querry_container { \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"     border: 1px solid gray; \n"
"     border-radius: 7px; \n"
" } "))
        self.widget_querry_container.setObjectName(_fromUtf8("widget_querry_container"))
        self.line_edit_querry = QtGui.QLineEdit(self.widget_querry_container)
        self.line_edit_querry.setGeometry(QtCore.QRect(20, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_edit_querry.setFont(font)
        self.line_edit_querry.setFrame(False)
        self.line_edit_querry.setObjectName(_fromUtf8("line_edit_querry"))
        self.button_fetch_tweets = QtGui.QPushButton(self.widget_querry_container)
        self.button_fetch_tweets.setGeometry(QtCore.QRect(440, 10, 91, 27))
        self.button_fetch_tweets.setStyleSheet(_fromUtf8(""))
        self.button_fetch_tweets.setText(_fromUtf8(""))
        self.button_fetch_tweets.setObjectName(_fromUtf8("button_fetch_tweets"))
        self.label = QtGui.QLabel(widget_fetch_tweets)
        self.label.setGeometry(QtCore.QRect(57, 152, 81, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line_edit_tweet_count = QtGui.QLineEdit(widget_fetch_tweets)
        self.line_edit_tweet_count.setGeometry(QtCore.QRect(140, 151, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_tweet_count.sizePolicy().hasHeightForWidth())
        self.line_edit_tweet_count.setSizePolicy(sizePolicy)
        self.line_edit_tweet_count.setStyleSheet(_fromUtf8("border: 1px solid gray; "))
        self.line_edit_tweet_count.setFrame(False)
        self.line_edit_tweet_count.setObjectName(_fromUtf8("line_edit_tweet_count"))
        self.button_append_to_file = QtGui.QPushButton(widget_fetch_tweets)
        self.button_append_to_file.setGeometry(QtCore.QRect(280, 150, 75, 23))
        self.button_append_to_file.setObjectName(_fromUtf8("button_append_to_file"))
        self.button_save_tweets = QtGui.QPushButton(widget_fetch_tweets)
        self.button_save_tweets.setGeometry(QtCore.QRect(230, 140, 38, 38))
        self.button_save_tweets.setStyleSheet(_fromUtf8(""))
        self.button_save_tweets.setText(_fromUtf8(""))
        self.button_save_tweets.setObjectName(_fromUtf8("button_save_tweets"))

        self.retranslateUi(widget_fetch_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_fetch_tweets)

    def retranslateUi(self, widget_fetch_tweets):
        widget_fetch_tweets.setWindowTitle(_translate("widget_fetch_tweets", "Fetch Tweets", None))
        self.label.setText(_translate("widget_fetch_tweets", "Tweet count:", None))
        self.button_append_to_file.setText(_translate("widget_fetch_tweets", "Append to file", None))

