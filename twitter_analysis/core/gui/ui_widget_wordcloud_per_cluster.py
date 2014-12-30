# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_wordcloud_per_cluster.ui'
#
# Created: Sun Dec 28 10:13:58 2014
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

class Ui_widget_wordcloud(object):
    def setupUi(self, widget_wordcloud):
        widget_wordcloud.setObjectName(_fromUtf8("widget_wordcloud"))
        widget_wordcloud.resize(549, 389)
        self.label_wordcloud = QtGui.QLabel(widget_wordcloud)
        self.label_wordcloud.setGeometry(QtCore.QRect(0, 50, 551, 341))
        self.label_wordcloud.setStyleSheet(_fromUtf8(""))
        self.label_wordcloud.setText(_fromUtf8(""))
        self.label_wordcloud.setObjectName(_fromUtf8("label_wordcloud"))
        self.widget = QtGui.QWidget(widget_wordcloud)
        self.widget.setGeometry(QtCore.QRect(11, 11, 181, 24))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.hlayout_clusters = QtGui.QHBoxLayout(self.widget)
        self.hlayout_clusters.setMargin(0)
        self.hlayout_clusters.setObjectName(_fromUtf8("hlayout_clusters"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.hlayout_clusters.addWidget(self.label)
        self.combobox_wordcloud = QtGui.QComboBox(self.widget)
        self.combobox_wordcloud.setObjectName(_fromUtf8("combobox_wordcloud"))
        self.hlayout_clusters.addWidget(self.combobox_wordcloud)

        self.retranslateUi(widget_wordcloud)
        QtCore.QMetaObject.connectSlotsByName(widget_wordcloud)

    def retranslateUi(self, widget_wordcloud):
        widget_wordcloud.setWindowTitle(_translate("widget_wordcloud", "Form", None))
        self.label.setText(_translate("widget_wordcloud", "Clusters:", None))

