# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_sentiment_per_cluster.ui'
#
# Created: Wed May 27 15:14:31 2015
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

class Ui_widget_sentiment_per_cluster(object):
    def setupUi(self, widget_sentiment_per_cluster):
        widget_sentiment_per_cluster.setObjectName(_fromUtf8("widget_sentiment_per_cluster"))
        widget_sentiment_per_cluster.resize(779, 549)
        self.label_sentiment_percentage = QtGui.QLabel(widget_sentiment_per_cluster)
        self.label_sentiment_percentage.setGeometry(QtCore.QRect(10, 50, 761, 491))
        self.label_sentiment_percentage.setStyleSheet(_fromUtf8(""))
        self.label_sentiment_percentage.setText(_fromUtf8(""))
        self.label_sentiment_percentage.setObjectName(_fromUtf8("label_sentiment_percentage"))
        self.layoutWidget = QtGui.QWidget(widget_sentiment_per_cluster)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 20, 141, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.combo_cluster = QtGui.QComboBox(self.layoutWidget)
        self.combo_cluster.setObjectName(_fromUtf8("combo_cluster"))
        self.horizontalLayout.addWidget(self.combo_cluster)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(widget_sentiment_per_cluster)
        QtCore.QMetaObject.connectSlotsByName(widget_sentiment_per_cluster)

    def retranslateUi(self, widget_sentiment_per_cluster):
        widget_sentiment_per_cluster.setWindowTitle(_translate("widget_sentiment_per_cluster", "Sentiment per cluster", None))
        self.label.setText(_translate("widget_sentiment_per_cluster", "Cluster:", None))

