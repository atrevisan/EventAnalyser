# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_wordcloud.ui'
#
# Created: Fri Dec 12 10:13:29 2014
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

class Ui_widgetWordCloud(object):
    def setupUi(self, widgetWordCloud):
        widgetWordCloud.setObjectName(_fromUtf8("widgetWordCloud"))
        widgetWordCloud.resize(549, 389)
        self.horizontalLayout = QtGui.QHBoxLayout(widgetWordCloud)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelWordCloud = QtGui.QLabel(widgetWordCloud)
        self.labelWordCloud.setText(_fromUtf8(""))
        self.labelWordCloud.setObjectName(_fromUtf8("labelWordCloud"))
        self.horizontalLayout.addWidget(self.labelWordCloud)

        self.retranslateUi(widgetWordCloud)
        QtCore.QMetaObject.connectSlotsByName(widgetWordCloud)

    def retranslateUi(self, widgetWordCloud):
        widgetWordCloud.setWindowTitle(_translate("widgetWordCloud", "Form", None))

