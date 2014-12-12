# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_analyse_tweets.ui'
#
# Created: Fri Dec 12 10:12:48 2014
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

class Ui_widgetAnalyseTweets(object):
    def setupUi(self, widgetAnalyseTweets):
        widgetAnalyseTweets.setObjectName(_fromUtf8("widgetAnalyseTweets"))
        widgetAnalyseTweets.resize(800, 500)
        self.horizontalLayout = QtGui.QHBoxLayout(widgetAnalyseTweets)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widgetMainWidget = QtGui.QWidget(widgetAnalyseTweets)
        self.widgetMainWidget.setObjectName(_fromUtf8("widgetMainWidget"))
        self.comboBoxTweets = QtGui.QComboBox(self.widgetMainWidget)
        self.comboBoxTweets.setGeometry(QtCore.QRect(140, 30, 131, 22))
        self.comboBoxTweets.setObjectName(_fromUtf8("comboBoxTweets"))
        self.label_2 = QtGui.QLabel(self.widgetMainWidget)
        self.label_2.setGeometry(QtCore.QRect(360, 27, 155, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonClusterize = QtGui.QPushButton(self.widgetMainWidget)
        self.pushButtonClusterize.setGeometry(QtCore.QRect(620, 27, 93, 28))
        self.pushButtonClusterize.setObjectName(_fromUtf8("pushButtonClusterize"))
        self.label = QtGui.QLabel(self.widgetMainWidget)
        self.label.setGeometry(QtCore.QRect(11, 27, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditClusters = QtGui.QLineEdit(self.widgetMainWidget)
        self.lineEditClusters.setGeometry(QtCore.QRect(530, 30, 51, 22))
        self.lineEditClusters.setObjectName(_fromUtf8("lineEditClusters"))
        self.verticalLayoutWidget = QtGui.QWidget(self.widgetMainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 191, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vLayoutButtons = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayoutButtons.setMargin(0)
        self.vLayoutButtons.setObjectName(_fromUtf8("vLayoutButtons"))
        self.pushButtonWordCloud = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWordCloud.setObjectName(_fromUtf8("pushButtonWordCloud"))
        self.vLayoutButtons.addWidget(self.pushButtonWordCloud)
        self.pushButtonSentiment = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSentiment.setObjectName(_fromUtf8("pushButtonSentiment"))
        self.vLayoutButtons.addWidget(self.pushButtonSentiment)
        self.pushButtonRelevantTweets = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonRelevantTweets.setObjectName(_fromUtf8("pushButtonRelevantTweets"))
        self.vLayoutButtons.addWidget(self.pushButtonRelevantTweets)
        self.pushButtonNGrams = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonNGrams.setObjectName(_fromUtf8("pushButtonNGrams"))
        self.vLayoutButtons.addWidget(self.pushButtonNGrams)
        self.pushButtonWordCloudPerCluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWordCloudPerCluster.setObjectName(_fromUtf8("pushButtonWordCloudPerCluster"))
        self.vLayoutButtons.addWidget(self.pushButtonWordCloudPerCluster)
        self.pushButtonSentimentPerCluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSentimentPerCluster.setObjectName(_fromUtf8("pushButtonSentimentPerCluster"))
        self.vLayoutButtons.addWidget(self.pushButtonSentimentPerCluster)
        self.pushButtonRelevantTweetsPerCluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonRelevantTweetsPerCluster.setObjectName(_fromUtf8("pushButtonRelevantTweetsPerCluster"))
        self.vLayoutButtons.addWidget(self.pushButtonRelevantTweetsPerCluster)
        self.pushButtonNGramsPerCluster = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonNGramsPerCluster.setObjectName(_fromUtf8("pushButtonNGramsPerCluster"))
        self.vLayoutButtons.addWidget(self.pushButtonNGramsPerCluster)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.widgetMainWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 551, 391))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vLayoutContents = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayoutContents.setMargin(0)
        self.vLayoutContents.setObjectName(_fromUtf8("vLayoutContents"))
        self.horizontalLayout.addWidget(self.widgetMainWidget)

        self.retranslateUi(widgetAnalyseTweets)
        QtCore.QMetaObject.connectSlotsByName(widgetAnalyseTweets)

    def retranslateUi(self, widgetAnalyseTweets):
        widgetAnalyseTweets.setWindowTitle(_translate("widgetAnalyseTweets", "Analyse Tweets", None))
        self.label_2.setText(_translate("widgetAnalyseTweets", "Number of clusters:", None))
        self.pushButtonClusterize.setText(_translate("widgetAnalyseTweets", "clusterize", None))
        self.label.setText(_translate("widgetAnalyseTweets", "Twitter dataset:", None))
        self.pushButtonWordCloud.setText(_translate("widgetAnalyseTweets", "Wordcloud", None))
        self.pushButtonSentiment.setText(_translate("widgetAnalyseTweets", "Sentiment", None))
        self.pushButtonRelevantTweets.setText(_translate("widgetAnalyseTweets", "Relevant tweets", None))
        self.pushButtonNGrams.setText(_translate("widgetAnalyseTweets", "N-grams", None))
        self.pushButtonWordCloudPerCluster.setText(_translate("widgetAnalyseTweets", "Wordcloud per cluster", None))
        self.pushButtonSentimentPerCluster.setText(_translate("widgetAnalyseTweets", "Sentiment per cluster", None))
        self.pushButtonRelevantTweetsPerCluster.setText(_translate("widgetAnalyseTweets", "Relevant tweets per cluster", None))
        self.pushButtonNGramsPerCluster.setText(_translate("widgetAnalyseTweets", "N-grams per cluster", None))

