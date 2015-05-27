# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_sentiment.ui'
#
# Created: Wed May 27 15:15:02 2015
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

class Ui_widget_sentiment(object):
    def setupUi(self, widget_sentiment):
        widget_sentiment.setObjectName(_fromUtf8("widget_sentiment"))
        widget_sentiment.resize(779, 549)
        self.label_sentiment_percentage = QtGui.QLabel(widget_sentiment)
        self.label_sentiment_percentage.setGeometry(QtCore.QRect(10, 50, 761, 491))
        self.label_sentiment_percentage.setStyleSheet(_fromUtf8(""))
        self.label_sentiment_percentage.setText(_fromUtf8(""))
        self.label_sentiment_percentage.setObjectName(_fromUtf8("label_sentiment_percentage"))

        self.retranslateUi(widget_sentiment)
        QtCore.QMetaObject.connectSlotsByName(widget_sentiment)

    def retranslateUi(self, widget_sentiment):
        widget_sentiment.setWindowTitle(_translate("widget_sentiment", "sentiment", None))

