# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_ngrams.ui'
#
# Created: Sun Jan 18 17:00:25 2015
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

class Ui_widget_ngrams(object):
    def setupUi(self, widget_ngrams):
        widget_ngrams.setObjectName(_fromUtf8("widget_ngrams"))
        widget_ngrams.resize(838, 709)
        self.label_graph = QtGui.QLabel(widget_ngrams)
        self.label_graph.setGeometry(QtCore.QRect(9, 80, 800, 600))
        self.label_graph.setStyleSheet(_fromUtf8(""))
        self.label_graph.setText(_fromUtf8(""))
        self.label_graph.setObjectName(_fromUtf8("label_graph"))
        self.layoutWidget = QtGui.QWidget(widget_ngrams)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 21, 185, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hlayout_radio = QtGui.QHBoxLayout(self.layoutWidget)
        self.hlayout_radio.setMargin(0)
        self.hlayout_radio.setObjectName(_fromUtf8("hlayout_radio"))
        self.radio_hour = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_hour.setFont(font)
        self.radio_hour.setObjectName(_fromUtf8("radio_hour"))
        self.hlayout_radio.addWidget(self.radio_hour)
        self.radio_day_week = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_day_week.setFont(font)
        self.radio_day_week.setObjectName(_fromUtf8("radio_day_week"))
        self.hlayout_radio.addWidget(self.radio_day_week)
        self.layoutWidget1 = QtGui.QWidget(widget_ngrams)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 10, 221, 57))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hlayout_ngrams = QtGui.QHBoxLayout()
        self.hlayout_ngrams.setObjectName(_fromUtf8("hlayout_ngrams"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hlayout_ngrams.addWidget(self.label_2)
        self.combo_ngrams = QtGui.QComboBox(self.layoutWidget1)
        self.combo_ngrams.setObjectName(_fromUtf8("combo_ngrams"))
        self.hlayout_ngrams.addWidget(self.combo_ngrams)
        self.hlayout_ngrams.setStretch(0, 1)
        self.hlayout_ngrams.setStretch(1, 6)
        self.verticalLayout.addLayout(self.hlayout_ngrams)

        self.retranslateUi(widget_ngrams)
        QtCore.QMetaObject.connectSlotsByName(widget_ngrams)

    def retranslateUi(self, widget_ngrams):
        widget_ngrams.setWindowTitle(_translate("widget_ngrams", "Form", None))
        self.radio_hour.setText(_translate("widget_ngrams", "hour", None))
        self.radio_day_week.setText(_translate("widget_ngrams", "day of week", None))
        self.label_2.setText(_translate("widget_ngrams", "N-grams:", None))

