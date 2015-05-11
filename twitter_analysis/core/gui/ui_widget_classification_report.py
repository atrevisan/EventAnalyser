# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_classification_report.ui'
#
# Created: Mon May 11 15:28:32 2015
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

class Ui_widget_classification_report(object):
    def setupUi(self, widget_classification_report):
        widget_classification_report.setObjectName(_fromUtf8("widget_classification_report"))
        widget_classification_report.resize(460, 387)
        self.verticalLayout = QtGui.QVBoxLayout(widget_classification_report)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.vlayout_table = QtGui.QVBoxLayout()
        self.vlayout_table.setObjectName(_fromUtf8("vlayout_table"))
        self.verticalLayout.addLayout(self.vlayout_table)
        self.button_ok = QtGui.QPushButton(widget_classification_report)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.verticalLayout.addWidget(self.button_ok)

        self.retranslateUi(widget_classification_report)
        QtCore.QMetaObject.connectSlotsByName(widget_classification_report)

    def retranslateUi(self, widget_classification_report):
        widget_classification_report.setWindowTitle(_translate("widget_classification_report", "Classification report", None))
        self.button_ok.setText(_translate("widget_classification_report", "ok", None))

