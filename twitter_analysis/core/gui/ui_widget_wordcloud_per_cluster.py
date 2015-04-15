# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_wordcloud_per_cluster.ui'
#
# Created: Wed Apr 15 10:39:26 2015
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

class Ui_widget_wordcloud_per_cluster(object):
    def setupUi(self, widget_wordcloud_per_cluster):
        widget_wordcloud_per_cluster.setObjectName(_fromUtf8("widget_wordcloud_per_cluster"))
        widget_wordcloud_per_cluster.resize(779, 549)
        self.label_wordcloud = QtGui.QLabel(widget_wordcloud_per_cluster)
        self.label_wordcloud.setGeometry(QtCore.QRect(10, 50, 761, 491))
        self.label_wordcloud.setStyleSheet(_fromUtf8("QLabel#label_wordcloud { \n"
"    background-color: rgb(234, 234, 234);\n"
" \n"
" } "))
        self.label_wordcloud.setText(_fromUtf8(""))
        self.label_wordcloud.setObjectName(_fromUtf8("label_wordcloud"))
        self.layoutWidget = QtGui.QWidget(widget_wordcloud_per_cluster)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 221, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hlayout_clusters = QtGui.QHBoxLayout(self.layoutWidget)
        self.hlayout_clusters.setMargin(0)
        self.hlayout_clusters.setObjectName(_fromUtf8("hlayout_clusters"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.hlayout_clusters.addWidget(self.label)
        self.combobox_cluster = QtGui.QComboBox(self.layoutWidget)
        self.combobox_cluster.setObjectName(_fromUtf8("combobox_cluster"))
        self.hlayout_clusters.addWidget(self.combobox_cluster)
        self.hlayout_clusters.setStretch(1, 1)

        self.retranslateUi(widget_wordcloud_per_cluster)
        QtCore.QMetaObject.connectSlotsByName(widget_wordcloud_per_cluster)

    def retranslateUi(self, widget_wordcloud_per_cluster):
        widget_wordcloud_per_cluster.setWindowTitle(_translate("widget_wordcloud_per_cluster", "Form", None))
        self.label.setText(_translate("widget_wordcloud_per_cluster", "Cluster:", None))

