# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_fetch_tweets.ui'
#
# Created: Mon Dec 22 20:27:43 2014
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
        self.widget_querry_container.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget_querry_container.setObjectName(_fromUtf8("widget_querry_container"))
        self.button_fetch_tweets = QtGui.QPushButton(self.widget_querry_container)
        self.button_fetch_tweets.setGeometry(QtCore.QRect(438, 10, 91, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_fetch_tweets.sizePolicy().hasHeightForWidth())
        self.button_fetch_tweets.setSizePolicy(sizePolicy)
        self.button_fetch_tweets.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.button_fetch_tweets.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("mg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_fetch_tweets.setIcon(icon)
        self.button_fetch_tweets.setObjectName(_fromUtf8("button_fetch_tweets"))
        self.line_edit_querry = QtGui.QLineEdit(self.widget_querry_container)
        self.line_edit_querry.setGeometry(QtCore.QRect(12, 12, 411, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_querry.sizePolicy().hasHeightForWidth())
        self.line_edit_querry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_querry.setFont(font)
        self.line_edit_querry.setStyleSheet(_fromUtf8(" qproperty-frame: false "))
        self.line_edit_querry.setObjectName(_fromUtf8("line_edit_querry"))
        self.button_save_tweets = QtGui.QPushButton(widget_fetch_tweets)
        self.button_save_tweets.setGeometry(QtCore.QRect(360, 148, 33, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save_tweets.sizePolicy().hasHeightForWidth())
        self.button_save_tweets.setSizePolicy(sizePolicy)
        self.button_save_tweets.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save_tweets.setIcon(icon1)
        self.button_save_tweets.setIconSize(QtCore.QSize(20, 20))
        self.button_save_tweets.setObjectName(_fromUtf8("button_save_tweets"))
        self.button_stop_fetching = QtGui.QPushButton(widget_fetch_tweets)
        self.button_stop_fetching.setGeometry(QtCore.QRect(315, 148, 33, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_stop_fetching.sizePolicy().hasHeightForWidth())
        self.button_stop_fetching.setSizePolicy(sizePolicy)
        self.button_stop_fetching.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_stop_fetching.setIcon(icon2)
        self.button_stop_fetching.setObjectName(_fromUtf8("button_stop_fetching"))
        self.label = QtGui.QLabel(widget_fetch_tweets)
        self.label.setGeometry(QtCore.QRect(57, 152, 97, 21))
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
        self.line_edit_tweet_count.setGeometry(QtCore.QRect(166, 151, 137, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_tweet_count.sizePolicy().hasHeightForWidth())
        self.line_edit_tweet_count.setSizePolicy(sizePolicy)
        self.line_edit_tweet_count.setObjectName(_fromUtf8("line_edit_tweet_count"))

        self.retranslateUi(widget_fetch_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_fetch_tweets)

    def retranslateUi(self, widget_fetch_tweets):
        widget_fetch_tweets.setWindowTitle(_translate("widget_fetch_tweets", "Fetch Tweets", None))
        self.button_fetch_tweets.setToolTip(_translate("widget_fetch_tweets", "search", None))
        self.button_save_tweets.setToolTip(_translate("widget_fetch_tweets", "save to csv", None))
        self.button_stop_fetching.setToolTip(_translate("widget_fetch_tweets", "stop fetching", None))
        self.label.setText(_translate("widget_fetch_tweets", "Tweet count:", None))

