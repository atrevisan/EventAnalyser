# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_analyse_tweets.ui'
#
# Created: Sun Jan 18 15:24:57 2015
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
        widget_analyse_tweets.resize(1100, 826)
        self.horizontalLayout = QtGui.QHBoxLayout(widget_analyse_tweets)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_main_widget = QtGui.QWidget(widget_analyse_tweets)
        self.widget_main_widget.setObjectName(_fromUtf8("widget_main_widget"))
        self.label = QtGui.QLabel(self.widget_main_widget)
        self.label.setGeometry(QtCore.QRect(12, 21, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(self.widget_main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 191, 415))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_buttons = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_buttons.setMargin(0)
        self.vlayout_buttons.setObjectName(_fromUtf8("vlayout_buttons"))
        self.button_wordcloud = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_wordcloud.setObjectName(_fromUtf8("button_wordcloud"))
        self.vlayout_buttons.addWidget(self.button_wordcloud)
        self.button_wordcloud_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_wordcloud_per_cluster.setObjectName(_fromUtf8("button_wordcloud_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_wordcloud_per_cluster)
        self.button_sentiment = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_sentiment.setObjectName(_fromUtf8("button_sentiment"))
        self.vlayout_buttons.addWidget(self.button_sentiment)
        self.button_sentiment_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_sentiment_per_cluster.setObjectName(_fromUtf8("button_sentiment_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_sentiment_per_cluster)
        self.button_relevant_tweets = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_relevant_tweets.setObjectName(_fromUtf8("button_relevant_tweets"))
        self.vlayout_buttons.addWidget(self.button_relevant_tweets)
        self.button_relevant_tweets_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_relevant_tweets_per_cluster.setObjectName(_fromUtf8("button_relevant_tweets_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_relevant_tweets_per_cluster)
        self.button_n_grams = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_n_grams.setObjectName(_fromUtf8("button_n_grams"))
        self.vlayout_buttons.addWidget(self.button_n_grams)
        self.button_n_grams_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_n_grams_per_cluster.setObjectName(_fromUtf8("button_n_grams_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_n_grams_per_cluster)
        self.button_retweets = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_retweets.setObjectName(_fromUtf8("button_retweets"))
        self.vlayout_buttons.addWidget(self.button_retweets)
        self.button_retweets_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_retweets_per_cluster.setObjectName(_fromUtf8("button_retweets_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_retweets_per_cluster)
        self.button_hashtags = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_hashtags.setObjectName(_fromUtf8("button_hashtags"))
        self.vlayout_buttons.addWidget(self.button_hashtags)
        self.button_hashtags_per_cluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_hashtags_per_cluster.setObjectName(_fromUtf8("button_hashtags_per_cluster"))
        self.vlayout_buttons.addWidget(self.button_hashtags_per_cluster)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.widget_main_widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 841, 711))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vlayout_content = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayout_content.setMargin(0)
        self.vlayout_content.setObjectName(_fromUtf8("vlayout_content"))
        self.button_open_file = QtGui.QPushButton(self.widget_main_widget)
        self.button_open_file.setGeometry(QtCore.QRect(141, 21, 41, 28))
        self.button_open_file.setStyleSheet(_fromUtf8(""))
        self.button_open_file.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../assets/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_open_file.setIcon(icon)
        self.button_open_file.setIconSize(QtCore.QSize(41, 28))
        self.button_open_file.setObjectName(_fromUtf8("button_open_file"))
        self.horizontalLayout.addWidget(self.widget_main_widget)

        self.retranslateUi(widget_analyse_tweets)
        QtCore.QMetaObject.connectSlotsByName(widget_analyse_tweets)

    def retranslateUi(self, widget_analyse_tweets):
        widget_analyse_tweets.setWindowTitle(_translate("widget_analyse_tweets", "Analyse Tweets", None))
        self.label.setText(_translate("widget_analyse_tweets", "Twitter dataset:", None))
        self.button_wordcloud.setText(_translate("widget_analyse_tweets", "Wordcloud", None))
        self.button_wordcloud_per_cluster.setText(_translate("widget_analyse_tweets", "Wordcloud per cluster", None))
        self.button_sentiment.setText(_translate("widget_analyse_tweets", "Sentiment", None))
        self.button_sentiment_per_cluster.setText(_translate("widget_analyse_tweets", "Sentiment per cluster", None))
        self.button_relevant_tweets.setText(_translate("widget_analyse_tweets", "Relevant tweets", None))
        self.button_relevant_tweets_per_cluster.setText(_translate("widget_analyse_tweets", "Relevant tweets per cluster", None))
        self.button_n_grams.setText(_translate("widget_analyse_tweets", "N-grams", None))
        self.button_n_grams_per_cluster.setText(_translate("widget_analyse_tweets", "N-grams per cluster", None))
        self.button_retweets.setText(_translate("widget_analyse_tweets", "Retweets", None))
        self.button_retweets_per_cluster.setText(_translate("widget_analyse_tweets", "Retweets per cluster", None))
        self.button_hashtags.setText(_translate("widget_analyse_tweets", "Hashtags", None))
        self.button_hashtags_per_cluster.setText(_translate("widget_analyse_tweets", "Hashtags per cluster", None))
        self.button_open_file.setToolTip(_translate("widget_analyse_tweets", "open", None))

