# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_cosine_similarity.ui'
#
# Created: Wed Apr 15 10:39:54 2015
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

class Ui_widget_cosine_similarity(object):
    def setupUi(self, widget_cosine_similarity):
        widget_cosine_similarity.setObjectName(_fromUtf8("widget_cosine_similarity"))
        widget_cosine_similarity.resize(800, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(widget_cosine_similarity.sizePolicy().hasHeightForWidth())
        widget_cosine_similarity.setSizePolicy(sizePolicy)
        widget_cosine_similarity.setStatusTip(_fromUtf8(""))
        widget_cosine_similarity.setWhatsThis(_fromUtf8(""))
        self.widget_querry_container = QtGui.QWidget(widget_cosine_similarity)
        self.widget_querry_container.setGeometry(QtCore.QRect(20, 20, 541, 41))
        self.widget_querry_container.setMaximumSize(QtCore.QSize(16777215, 51))
        self.widget_querry_container.setStyleSheet(_fromUtf8("\n"
"\n"
"QWidget#widget_querry_container { \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"     border: 1px solid gray; \n"
"     border-radius: 7px; \n"
" } "))
        self.widget_querry_container.setObjectName(_fromUtf8("widget_querry_container"))
        self.line_edit_querry = QtGui.QLineEdit(self.widget_querry_container)
        self.line_edit_querry.setGeometry(QtCore.QRect(20, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_edit_querry.setFont(font)
        self.line_edit_querry.setFrame(False)
        self.line_edit_querry.setObjectName(_fromUtf8("line_edit_querry"))
        self.button_fetch_tweets = QtGui.QPushButton(self.widget_querry_container)
        self.button_fetch_tweets.setGeometry(QtCore.QRect(440, 10, 91, 27))
        self.button_fetch_tweets.setStyleSheet(_fromUtf8(""))
        self.button_fetch_tweets.setText(_fromUtf8(""))
        self.button_fetch_tweets.setObjectName(_fromUtf8("button_fetch_tweets"))
        self.text_edit_most_relevant_tweets = QtGui.QTextEdit(widget_cosine_similarity)
        self.text_edit_most_relevant_tweets.setGeometry(QtCore.QRect(30, 110, 521, 331))
        self.text_edit_most_relevant_tweets.setObjectName(_fromUtf8("text_edit_most_relevant_tweets"))

        self.retranslateUi(widget_cosine_similarity)
        QtCore.QMetaObject.connectSlotsByName(widget_cosine_similarity)

    def retranslateUi(self, widget_cosine_similarity):
        widget_cosine_similarity.setWindowTitle(_translate("widget_cosine_similarity", "Search most relevant tweets", None))

