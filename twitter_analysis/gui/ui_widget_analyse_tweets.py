# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_analyse_tweets.ui'
#
# Created: Mon Dec 22 13:18:12 2014
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

class Ui_widget_analyse_tweets(object):
    def setupUi(self, widget_analyse_tweets):
        widget_analyse_tweets.setObjectName(_fromUtf8("widget_analyse_tweets"))
        widget_analyse_tweets.resize(800, 500)
        self.horizontalLayout = QtGui.QHBoxLayout(widget_analyse_tweets)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_main_widget = QtGui.QWidget(widget_analyse_tweets)
        self.widget_main_widget.setObjectName(_fromUtf8("widget_main_widget"))
        self.combo_box_datasets = QtGui.QComboBox(self.widget_main_widget)
        self.combo_box_datasets.setGeometry(QtCore.QRect(140, 30, 131, 22))
        self.combo_box_datasets.setObjectName(_fromUtf8("combo_box_datasets"))
        self.label_2 = QtGui.QLabel(self.widget_main_widget)
        self.label_2.setGeometry(QtCore.QRect(360, 27, 155, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_clusterize = QtGui.QPushButton(self.widget_main_widget)
        self.button_clusterize.setGeometry(QtCore.QRect(620, 27, 93, 28))
        self.button_clusterize.setObjectName(_fromUtf8("button_clusterize"))
        self.label = QtGui.QLabel(self.widget_main_widget)
        self.label.setGeometry(QtCore.QRect(11, 27, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line_edit_clusters = QtGui.QLineEdit(self.widget_main_widget)
        self.line_edit_clusters.setGeometry(QtCore.QRect(530, 30, 51, 22))
        self.line_edit_clusters.setObjectName(_fromUtf8("line_edit_clusters"))
        self.verticalLayoutWidget = QtGui.QWidget(self.widget_main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 191, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_buttons = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_buttons.setMargin(0)
        self.vlayout_buttons.setObjectName(_fromUtf8("vlayout_buttons"))
        self.button_word_cloud = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_word_cloud.setObjectName(_fromUtf8("button_word_cloud"))
        self.vlayout_buttons.addWidget(self.button_word_cloud)
        self.button_sentiment = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_sentiment.setObjectName(_fromUtf8("button_sentiment"))
        self.vlayout_buttons.addWidget(self.button_sentiment)
        self.button_relevant_tweets = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_relevant_tweets.setObjectName(_fromUtf8("button_relevant_tweets"))
        self.vlayout_buttons.addWidget(self.button_relevant_tweets)
        self.button_n_grams = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_n_grams.setObjectName(_fromUtf8("button_n_grams"))
        self.vlayout_buttons.addWidget(self.button_n_grams)
        self.button_wordcloud_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_wordcloud_per_cluster.setObjectName(_fromUtf8("button_wordcloud_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_wordcloud_per_cluster)
        self.button_sentiment_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_sentiment_per_cluster.setObjectName(_fromUtf8("button_sentiment_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_sentiment_per_cluster)
        self.button_relevant_tweets_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_relevant_tweets_per_cluster.setObjectName(_fromUtf8("button_relevant_tweets_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_relevant_tweets_per_cluster)
        self.button_n_grams_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_n_grams_per_cluster.setObjectName(_fromUtf8("button_n_grams_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_n_grams_per_cluster)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.widget_main_widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 551, 391))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vLayoutContent = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayoutContent.setMargin(0)
        self.vLayoutContent.setObjectName(_fromUtf8("vLayoutContent"))
        self.horizontalLayout.addWidget(self.widget_main_widget)

        self.retranslateUi(widget_analyse_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_analyse_tweets)

    def retranslateUi(self, widget_analyse_tweets):
        widget_analyse_tweets.setWindowTitle(_translate("widget_analyse_tweets", "Analyse Tweets", None))
        self.label_2.setText(_translate("widget_analyse_tweets", "Number of clusters:", None))
        self.button_clusterize.setText(_translate("widget_analyse_tweets", "clusterize", None))
        self.label.setText(_translate("widget_analyse_tweets", "Twitter dataset:", None))
        self.button_word_cloud.setText(_translate("widget_analyse_tweets", "Wordcloud", None))
        self.button_sentiment.setText(_translate("widget_analyse_tweets", "Sentiment", None))
        self.button_relevant_tweets.setText(_translate("widget_analyse_tweets", "Relevant tweets", None))
        self.button_n_grams.setText(_translate("widget_analyse_tweets", "N-grams", None))
        self.button_wordcloud_per_cluster.setText(_translate("widget_analyse_tweets", "Wordcloud per cluster", None))
        self.button_sentiment_per_cluster.setText(_translate("widget_analyse_tweets", "Sentiment per cluster", None))
        self.button_relevant_tweets_per_cluster.setText(_translate("widget_analyse_tweets", "Relevant tweets per cluster", None))
        self.button_n_grams_per_cluster.setText(_translate("widget_analyse_tweets", "N-grams per cluster", None))

