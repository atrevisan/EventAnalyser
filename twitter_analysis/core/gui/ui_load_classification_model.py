# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_load_classification_model.ui'
#
# Created: Fri Apr 10 11:55:09 2015
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

class Ui_widget_load_sentiment_classification_model(object):
    def setupUi(self, widget_load_sentiment_classification_model):
        widget_load_sentiment_classification_model.setObjectName(_fromUtf8("widget_load_sentiment_classification_model"))
        widget_load_sentiment_classification_model.resize(800, 600)
        self.button_open_file = QtGui.QPushButton(widget_load_sentiment_classification_model)
        self.button_open_file.setGeometry(QtCore.QRect(490, 20, 71, 23))
        self.button_open_file.setStyleSheet(_fromUtf8(""))
        self.button_open_file.setIconSize(QtCore.QSize(53, 36))
        self.button_open_file.setObjectName(_fromUtf8("button_open_file"))
        self.layoutWidget = QtGui.QWidget(widget_load_sentiment_classification_model)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 21, 471, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet(_fromUtf8("border: 1px solid gray; "))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(widget_load_sentiment_classification_model)
        QtCore.QMetaObject.connectSlotsByName(widget_load_sentiment_classification_model)

    def retranslateUi(self, widget_load_sentiment_classification_model):
        widget_load_sentiment_classification_model.setWindowTitle(_translate("widget_load_sentiment_classification_model", "Form", None))
        self.button_open_file.setToolTip(_translate("widget_load_sentiment_classification_model", "open", None))
        self.button_open_file.setText(_translate("widget_load_sentiment_classification_model", "Browse...", None))
        self.label.setText(_translate("widget_load_sentiment_classification_model", "Load classification model:", None))

