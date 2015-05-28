# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu May 28 09:16:40 2015
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(800, 600)
        self.widget_central_widget = QtGui.QWidget(main_window)
        self.widget_central_widget.setStyleSheet(_fromUtf8(""))
        self.widget_central_widget.setObjectName(_fromUtf8("widget_central_widget"))
        main_window.setCentralWidget(self.widget_central_widget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_text_analysis = QtGui.QMenu(self.menubar)
        self.menu_text_analysis.setObjectName(_fromUtf8("menu_text_analysis"))
        self.menu_analyse_tweets = QtGui.QMenu(self.menu_text_analysis)
        self.menu_analyse_tweets.setObjectName(_fromUtf8("menu_analyse_tweets"))
        main_window.setMenuBar(self.menubar)
        self.action_fetch_tweets = QtGui.QAction(main_window)
        self.action_fetch_tweets.setObjectName(_fromUtf8("action_fetch_tweets"))
        self.action_clustering_config = QtGui.QAction(main_window)
        self.action_clustering_config.setObjectName(_fromUtf8("action_clustering_config"))
        self.action_text_analysis_config = QtGui.QAction(main_window)
        self.action_text_analysis_config.setObjectName(_fromUtf8("action_text_analysis_config"))
        self.action_wordcloud = QtGui.QAction(main_window)
        self.action_wordcloud.setObjectName(_fromUtf8("action_wordcloud"))
        self.action_wordcloud_per_cluster = QtGui.QAction(main_window)
        self.action_wordcloud_per_cluster.setObjectName(_fromUtf8("action_wordcloud_per_cluster"))
        self.action_sentiment = QtGui.QAction(main_window)
        self.action_sentiment.setObjectName(_fromUtf8("action_sentiment"))
        self.action_sentiment_per_cluster = QtGui.QAction(main_window)
        self.action_sentiment_per_cluster.setObjectName(_fromUtf8("action_sentiment_per_cluster"))
        self.action_relevant_tweets = QtGui.QAction(main_window)
        self.action_relevant_tweets.setObjectName(_fromUtf8("action_relevant_tweets"))
        self.action_relevant_tweets_per_cluster = QtGui.QAction(main_window)
        self.action_relevant_tweets_per_cluster.setObjectName(_fromUtf8("action_relevant_tweets_per_cluster"))
        self.action_ngrams = QtGui.QAction(main_window)
        self.action_ngrams.setObjectName(_fromUtf8("action_ngrams"))
        self.action_ngrams_per_cluster = QtGui.QAction(main_window)
        self.action_ngrams_per_cluster.setObjectName(_fromUtf8("action_ngrams_per_cluster"))
        self.action_sentiment_by_location = QtGui.QAction(main_window)
        self.action_sentiment_by_location.setObjectName(_fromUtf8("action_sentiment_by_location"))
        self.action_hashtags = QtGui.QAction(main_window)
        self.action_hashtags.setObjectName(_fromUtf8("action_hashtags"))
        self.action_hashtags_per_cluster = QtGui.QAction(main_window)
        self.action_hashtags_per_cluster.setObjectName(_fromUtf8("action_hashtags_per_cluster"))
        self.action_sentiment_classifier_config = QtGui.QAction(main_window)
        self.action_sentiment_classifier_config.setObjectName(_fromUtf8("action_sentiment_classifier_config"))
        self.action_load_dataset = QtGui.QAction(main_window)
        self.action_load_dataset.setObjectName(_fromUtf8("action_load_dataset"))
        self.actionLoad_sentiment_classification_model = QtGui.QAction(main_window)
        self.actionLoad_sentiment_classification_model.setObjectName(_fromUtf8("actionLoad_sentiment_classification_model"))
        self.action_cosine_similarity = QtGui.QAction(main_window)
        self.action_cosine_similarity.setObjectName(_fromUtf8("action_cosine_similarity"))
        self.menu_analyse_tweets.addAction(self.action_wordcloud)
        self.menu_analyse_tweets.addAction(self.action_wordcloud_per_cluster)
        self.menu_analyse_tweets.addAction(self.action_sentiment)
        self.menu_analyse_tweets.addAction(self.action_sentiment_per_cluster)
        self.menu_analyse_tweets.addAction(self.action_relevant_tweets)
        self.menu_analyse_tweets.addAction(self.action_relevant_tweets_per_cluster)
        self.menu_analyse_tweets.addAction(self.action_ngrams)
        self.menu_analyse_tweets.addAction(self.action_ngrams_per_cluster)
        self.menu_analyse_tweets.addAction(self.action_hashtags)
        self.menu_analyse_tweets.addAction(self.action_hashtags_per_cluster)
        self.menu_analyse_tweets.addAction(self.action_cosine_similarity)
        self.menu_text_analysis.addAction(self.action_fetch_tweets)
        self.menu_text_analysis.addAction(self.action_load_dataset)
        self.menu_text_analysis.addAction(self.actionLoad_sentiment_classification_model)
        self.menu_text_analysis.addAction(self.menu_analyse_tweets.menuAction())
        self.menu_text_analysis.addAction(self.action_clustering_config)
        self.menu_text_analysis.addAction(self.action_sentiment_classifier_config)
        self.menubar.addAction(self.menu_text_analysis.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Twitter text analyser", None))
        self.menu_text_analysis.setTitle(_translate("main_window", "Text analysis", None))
        self.menu_analyse_tweets.setTitle(_translate("main_window", "Analyse tweets", None))
        self.action_fetch_tweets.setText(_translate("main_window", "Fetch tweets", None))
        self.action_clustering_config.setText(_translate("main_window", "Clustering config", None))
        self.action_text_analysis_config.setText(_translate("main_window", "Text analysis config", None))
        self.action_wordcloud.setText(_translate("main_window", "wordcloud", None))
        self.action_wordcloud_per_cluster.setText(_translate("main_window", "wordcloud per cluster", None))
        self.action_sentiment.setText(_translate("main_window", "sentiment", None))
        self.action_sentiment_per_cluster.setText(_translate("main_window", "sentiment per cluster", None))
        self.action_relevant_tweets.setText(_translate("main_window", "relevant tweets", None))
        self.action_relevant_tweets_per_cluster.setText(_translate("main_window", "relevant tweets per cluster", None))
        self.action_ngrams.setText(_translate("main_window", "n-grams", None))
        self.action_ngrams_per_cluster.setText(_translate("main_window", "n-grams per cluster", None))
        self.action_sentiment_by_location.setText(_translate("main_window", "sentiment by location", None))
        self.action_hashtags.setText(_translate("main_window", "hashtags", None))
        self.action_hashtags_per_cluster.setText(_translate("main_window", "hashtags per cluster", None))
        self.action_sentiment_classifier_config.setText(_translate("main_window", "Sentiment classifier config", None))
        self.action_load_dataset.setText(_translate("main_window", "Load clusterized dataset", None))
        self.actionLoad_sentiment_classification_model.setText(_translate("main_window", "Load sentiment classification model", None))
        self.action_cosine_similarity.setText(_translate("main_window", "cosine similarity search", None))

