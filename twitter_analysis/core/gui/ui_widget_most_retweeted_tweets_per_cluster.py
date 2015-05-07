# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_most_retweeted_tweets_per_cluster.ui'
#
# Created: Fri Apr 17 11:13:50 2015
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

class Ui_widget_most_retweeted_tweets(object):
    def setupUi(self, widget_most_retweeted_tweets):
        widget_most_retweeted_tweets.setObjectName(_fromUtf8("widget_most_retweeted_tweets"))
        widget_most_retweeted_tweets.resize(800, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(widget_most_retweeted_tweets.sizePolicy().hasHeightForWidth())
        widget_most_retweeted_tweets.setSizePolicy(sizePolicy)
        widget_most_retweeted_tweets.setStatusTip(_fromUtf8(""))
        widget_most_retweeted_tweets.setWhatsThis(_fromUtf8(""))
        self.text_edit_most_retweeted_tweets = QtGui.QTextEdit(widget_most_retweeted_tweets)
        self.text_edit_most_retweeted_tweets.setGeometry(QtCore.QRect(30, 110, 521, 331))
        self.text_edit_most_retweeted_tweets.setObjectName(_fromUtf8("text_edit_most_retweeted_tweets"))
        self.label = QtGui.QLabel(widget_most_retweeted_tweets)
        self.label.setGeometry(QtCore.QRect(40, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(widget_most_retweeted_tweets)
        self.widget.setGeometry(QtCore.QRect(10, 10, 181, 22))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.combo_cluster = QtGui.QComboBox(self.widget)
        self.combo_cluster.setObjectName(_fromUtf8("combo_cluster"))
        self.horizontalLayout.addWidget(self.combo_cluster)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(widget_most_retweeted_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_most_retweeted_tweets)

    def retranslateUi(self, widget_most_retweeted_tweets):
        widget_most_retweeted_tweets.setWindowTitle(_translate("widget_most_retweeted_tweets", "Most retweeted tweets", None))
        self.label.setText(_translate("widget_most_retweeted_tweets", "Most retweeted tweets", None))
        self.label_2.setText(_translate("widget_most_retweeted_tweets", "Cluster:", None))

