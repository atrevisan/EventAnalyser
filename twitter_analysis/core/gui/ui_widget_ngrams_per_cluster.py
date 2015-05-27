# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_ngrams_per_cluster.ui'
#
# Created: Wed May 27 12:03:52 2015
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

class Ui_widget_ngrams_per_cluster(object):
    def setupUi(self, widget_ngrams_per_cluster):
        widget_ngrams_per_cluster.setObjectName(_fromUtf8("widget_ngrams_per_cluster"))
        widget_ngrams_per_cluster.resize(800, 549)
        self.label_graph = QtGui.QLabel(widget_ngrams_per_cluster)
        self.label_graph.setGeometry(QtCore.QRect(190, 70, 591, 451))
        self.label_graph.setStyleSheet(_fromUtf8("QLabel#label_graph { \n"
"    background-color: rgb(234, 234, 234);\n"
"     border: 2px solid gray; \n"
"  \n"
" } "))
        self.label_graph.setText(_fromUtf8(""))
        self.label_graph.setObjectName(_fromUtf8("label_graph"))
        self.layoutWidget = QtGui.QWidget(widget_ngrams_per_cluster)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 11, 201, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hlayout_ngrams = QtGui.QHBoxLayout(self.layoutWidget)
        self.hlayout_ngrams.setMargin(0)
        self.hlayout_ngrams.setObjectName(_fromUtf8("hlayout_ngrams"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hlayout_ngrams.addWidget(self.label_2)
        self.combo_ngrams = QtGui.QComboBox(self.layoutWidget)
        self.combo_ngrams.setObjectName(_fromUtf8("combo_ngrams"))
        self.hlayout_ngrams.addWidget(self.combo_ngrams)
        self.hlayout_ngrams.setStretch(0, 1)
        self.hlayout_ngrams.setStretch(1, 6)
        self.widget = QtGui.QWidget(widget_ngrams_per_cluster)
        self.widget.setGeometry(QtCore.QRect(30, 100, 137, 106))
        self.widget.setStyleSheet(_fromUtf8("QWidget#widget { \n"
"    background-color: rgb(234, 234, 234);\n"
"     border: 1px solid gray; \n"
"  \n"
" } "))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radio_frequency = QtGui.QRadioButton(self.widget)
        self.radio_frequency.setObjectName(_fromUtf8("radio_frequency"))
        self.verticalLayout_2.addWidget(self.radio_frequency)
        self.radio_retweets = QtGui.QRadioButton(self.widget)
        self.radio_retweets.setObjectName(_fromUtf8("radio_retweets"))
        self.verticalLayout_2.addWidget(self.radio_retweets)
        self.radio_positive_sentiment = QtGui.QRadioButton(self.widget)
        self.radio_positive_sentiment.setObjectName(_fromUtf8("radio_positive_sentiment"))
        self.verticalLayout_2.addWidget(self.radio_positive_sentiment)
        self.radio_negative_sentiment = QtGui.QRadioButton(self.widget)
        self.radio_negative_sentiment.setObjectName(_fromUtf8("radio_negative_sentiment"))
        self.verticalLayout_2.addWidget(self.radio_negative_sentiment)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.widget_2 = QtGui.QWidget(widget_ngrams_per_cluster)
        self.widget_2.setGeometry(QtCore.QRect(30, 250, 137, 185))
        self.widget_2.setStyleSheet(_fromUtf8("QWidget#widget_2 { \n"
"    background-color: rgb(234, 234, 234);\n"
"\n"
"       border: 1px solid gray; \n"
" } "))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.combo_year = QtGui.QComboBox(self.widget_2)
        self.combo_year.setObjectName(_fromUtf8("combo_year"))
        self.horizontalLayout.addWidget(self.combo_year)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_info_per_month = QtGui.QPushButton(self.widget_2)
        self.button_info_per_month.setObjectName(_fromUtf8("button_info_per_month"))
        self.verticalLayout.addWidget(self.button_info_per_month)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.combo_month = QtGui.QComboBox(self.widget_2)
        self.combo_month.setObjectName(_fromUtf8("combo_month"))
        self.horizontalLayout_2.addWidget(self.combo_month)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.button_info_per_day = QtGui.QPushButton(self.widget_2)
        self.button_info_per_day.setObjectName(_fromUtf8("button_info_per_day"))
        self.verticalLayout.addWidget(self.button_info_per_day)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.combo_day = QtGui.QComboBox(self.widget_2)
        self.combo_day.setObjectName(_fromUtf8("combo_day"))
        self.horizontalLayout_3.addWidget(self.combo_day)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.button_info_per_hour = QtGui.QPushButton(self.widget_2)
        self.button_info_per_hour.setObjectName(_fromUtf8("button_info_per_hour"))
        self.verticalLayout.addWidget(self.button_info_per_hour)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.widget1 = QtGui.QWidget(widget_ngrams_per_cluster)
        self.widget1.setGeometry(QtCore.QRect(210, 11, 161, 22))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.combo_cluster = QtGui.QComboBox(self.widget1)
        self.combo_cluster.setObjectName(_fromUtf8("combo_cluster"))
        self.horizontalLayout_6.addWidget(self.combo_cluster)
        self.horizontalLayout_6.setStretch(1, 1)

        self.retranslateUi(widget_ngrams_per_cluster)
        QtCore.QMetaObject.connectSlotsByName(widget_ngrams_per_cluster)

    def retranslateUi(self, widget_ngrams_per_cluster):
        widget_ngrams_per_cluster.setWindowTitle(_translate("widget_ngrams_per_cluster", "Form", None))
        self.label_2.setText(_translate("widget_ngrams_per_cluster", "N-grams:", None))
        self.radio_frequency.setText(_translate("widget_ngrams_per_cluster", "Frequency", None))
        self.radio_retweets.setText(_translate("widget_ngrams_per_cluster", "Retweets", None))
        self.radio_positive_sentiment.setText(_translate("widget_ngrams_per_cluster", "Positive Sentiment", None))
        self.radio_negative_sentiment.setText(_translate("widget_ngrams_per_cluster", "Negative Sentiment", None))
        self.label.setText(_translate("widget_ngrams_per_cluster", "Year:", None))
        self.button_info_per_month.setText(_translate("widget_ngrams_per_cluster", "Info per month", None))
        self.label_3.setText(_translate("widget_ngrams_per_cluster", "Month:", None))
        self.button_info_per_day.setText(_translate("widget_ngrams_per_cluster", "Info per day", None))
        self.label_4.setText(_translate("widget_ngrams_per_cluster", "Day:", None))
        self.button_info_per_hour.setText(_translate("widget_ngrams_per_cluster", "Info per hour", None))
        self.label_5.setText(_translate("widget_ngrams_per_cluster", "Cluster:", None))

