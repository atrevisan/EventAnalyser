# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_sentiment_classifier_config.ui'
#
# Created: Fri Apr 24 14:34:26 2015
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

class Ui_widget_sentiment_classifier_config(object):
    def setupUi(self, widget_sentiment_classifier_config):
        widget_sentiment_classifier_config.setObjectName(_fromUtf8("widget_sentiment_classifier_config"))
        widget_sentiment_classifier_config.resize(800, 600)
        self.groupBox = QtGui.QGroupBox(widget_sentiment_classifier_config)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 641, 251))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox#groupBox { \n"
"    background-color: rgb(234, 234, 234);\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 59, 192, 119))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_16 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_15.addWidget(self.label_16)
        self.combo_ngram_range = QtGui.QComboBox(self.layoutWidget_3)
        self.combo_ngram_range.setObjectName(_fromUtf8("combo_ngram_range"))
        self.horizontalLayout_15.addWidget(self.combo_ngram_range)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_17 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_16.addWidget(self.label_17)
        self.combo_max_df = QtGui.QComboBox(self.layoutWidget_3)
        self.combo_max_df.setObjectName(_fromUtf8("combo_max_df"))
        self.horizontalLayout_16.addWidget(self.combo_max_df)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_18 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_17.addWidget(self.label_18)
        self.combo_min_df = QtGui.QComboBox(self.layoutWidget_3)
        self.combo_min_df.setObjectName(_fromUtf8("combo_min_df"))
        self.horizontalLayout_17.addWidget(self.combo_min_df)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_19 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_18.addWidget(self.label_19)
        self.combo_max_features = QtGui.QComboBox(self.layoutWidget_3)
        self.combo_max_features.setObjectName(_fromUtf8("combo_max_features"))
        self.horizontalLayout_18.addWidget(self.combo_max_features)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.button_vectorize = QtGui.QPushButton(self.groupBox)
        self.button_vectorize.setGeometry(QtCore.QRect(30, 210, 91, 23))
        self.button_vectorize.setObjectName(_fromUtf8("button_vectorize"))
        self.layoutWidget_4 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(370, 59, 195, 119))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.vlayout_checkboxes = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.vlayout_checkboxes.setMargin(0)
        self.vlayout_checkboxes.setObjectName(_fromUtf8("vlayout_checkboxes"))
        self.check_use_stemming = QtGui.QCheckBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_use_stemming.setFont(font)
        self.check_use_stemming.setObjectName(_fromUtf8("check_use_stemming"))
        self.vlayout_checkboxes.addWidget(self.check_use_stemming)
        self.check_use_idf = QtGui.QCheckBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_use_idf.setFont(font)
        self.check_use_idf.setObjectName(_fromUtf8("check_use_idf"))
        self.vlayout_checkboxes.addWidget(self.check_use_idf)
        self.check_binary = QtGui.QCheckBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_binary.setFont(font)
        self.check_binary.setObjectName(_fromUtf8("check_binary"))
        self.vlayout_checkboxes.addWidget(self.check_binary)
        self.check_remove_stopwords = QtGui.QCheckBox(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_remove_stopwords.setFont(font)
        self.check_remove_stopwords.setObjectName(_fromUtf8("check_remove_stopwords"))
        self.vlayout_checkboxes.addWidget(self.check_remove_stopwords)
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 19, 221, 24))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_15 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_7.addWidget(self.label_15)
        self.combo_vectorizer = QtGui.QComboBox(self.layoutWidget_2)
        self.combo_vectorizer.setObjectName(_fromUtf8("combo_vectorizer"))
        self.horizontalLayout_7.addWidget(self.combo_vectorizer)
        self.horizontalLayout_7.setStretch(1, 1)
        self.layoutWidget_5 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_5.setGeometry(QtCore.QRect(140, 209, 219, 31))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_19.setMargin(0)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_20 = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_19.addWidget(self.label_20)
        self.label_features = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_features.setFont(font)
        self.label_features.setStyleSheet(_fromUtf8(""))
        self.label_features.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_features.setText(_fromUtf8(""))
        self.label_features.setObjectName(_fromUtf8("label_features"))
        self.horizontalLayout_19.addWidget(self.label_features)
        self.horizontalLayout_19.setStretch(1, 1)
        self.groupBox_2 = QtGui.QGroupBox(widget_sentiment_classifier_config)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 340, 641, 201))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox#groupBox_2 { \n"
"     background-color: rgb(234, 234, 234);\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } "))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_8 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 20, 181, 24))
        self.layoutWidget_8.setObjectName(_fromUtf8("layoutWidget_8"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_24.setMargin(0)
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_25 = QtGui.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_24.addWidget(self.label_25)
        self.combo_classifier = QtGui.QComboBox(self.layoutWidget_8)
        self.combo_classifier.setObjectName(_fromUtf8("combo_classifier"))
        self.horizontalLayout_24.addWidget(self.combo_classifier)
        self.horizontalLayout_24.setStretch(1, 1)
        self.button_train = QtGui.QPushButton(self.groupBox_2)
        self.button_train.setGeometry(QtCore.QRect(20, 140, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_train.setFont(font)
        self.button_train.setObjectName(_fromUtf8("button_train"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 140, 191, 18))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_22.setMargin(0)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_23 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_22.addWidget(self.label_23)
        self.label_classification_time = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_classification_time.setFont(font)
        self.label_classification_time.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_classification_time.setText(_fromUtf8(""))
        self.label_classification_time.setObjectName(_fromUtf8("label_classification_time"))
        self.horizontalLayout_22.addWidget(self.label_classification_time)
        self.horizontalLayout_22.setStretch(1, 1)
        self.layoutWidget_6 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(390, 10, 221, 101))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.check_perform_lsa = QtGui.QCheckBox(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_perform_lsa.setFont(font)
        self.check_perform_lsa.setObjectName(_fromUtf8("check_perform_lsa"))
        self.verticalLayout_5.addWidget(self.check_perform_lsa)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_21 = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_20.addWidget(self.label_21)
        self.combo_num_of_components = QtGui.QComboBox(self.layoutWidget_6)
        self.combo_num_of_components.setObjectName(_fromUtf8("combo_num_of_components"))
        self.horizontalLayout_20.addWidget(self.combo_num_of_components)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_22 = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_21.addWidget(self.label_22)
        self.label_explained_variance = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_explained_variance.setFont(font)
        self.label_explained_variance.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_explained_variance.setText(_fromUtf8(""))
        self.label_explained_variance.setObjectName(_fromUtf8("label_explained_variance"))
        self.horizontalLayout_21.addWidget(self.label_explained_variance)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 88, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.combo_regularization = QtGui.QComboBox(self.layoutWidget1)
        self.combo_regularization.setObjectName(_fromUtf8("combo_regularization"))
        self.horizontalLayout_2.addWidget(self.combo_regularization)
        self.layoutWidget2 = QtGui.QWidget(widget_sentiment_classifier_config)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 210, 25))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.button_open_positive_sentiment_dataset = QtGui.QPushButton(self.layoutWidget2)
        self.button_open_positive_sentiment_dataset.setStyleSheet(_fromUtf8(""))
        self.button_open_positive_sentiment_dataset.setIconSize(QtCore.QSize(53, 36))
        self.button_open_positive_sentiment_dataset.setObjectName(_fromUtf8("button_open_positive_sentiment_dataset"))
        self.horizontalLayout.addWidget(self.button_open_positive_sentiment_dataset)
        self.button_save_sentiment_classifier_config = QtGui.QPushButton(widget_sentiment_classifier_config)
        self.button_save_sentiment_classifier_config.setGeometry(QtCore.QRect(670, 500, 38, 38))
        self.button_save_sentiment_classifier_config.setStyleSheet(_fromUtf8(""))
        self.button_save_sentiment_classifier_config.setText(_fromUtf8(""))
        self.button_save_sentiment_classifier_config.setObjectName(_fromUtf8("button_save_sentiment_classifier_config"))
        self.layoutWidget_7 = QtGui.QWidget(widget_sentiment_classifier_config)
        self.layoutWidget_7.setGeometry(QtCore.QRect(250, 10, 216, 25))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.button_open_negative_sentiment_dataset = QtGui.QPushButton(self.layoutWidget_7)
        self.button_open_negative_sentiment_dataset.setStyleSheet(_fromUtf8(""))
        self.button_open_negative_sentiment_dataset.setIconSize(QtCore.QSize(53, 36))
        self.button_open_negative_sentiment_dataset.setObjectName(_fromUtf8("button_open_negative_sentiment_dataset"))
        self.horizontalLayout_3.addWidget(self.button_open_negative_sentiment_dataset)

        self.retranslateUi(widget_sentiment_classifier_config)
        QtCore.QMetaObject.connectSlotsByName(widget_sentiment_classifier_config)

    def retranslateUi(self, widget_sentiment_classifier_config):
        widget_sentiment_classifier_config.setWindowTitle(_translate("widget_sentiment_classifier_config", "Form", None))
        self.groupBox.setTitle(_translate("widget_sentiment_classifier_config", "Feature extraction", None))
        self.label_16.setText(_translate("widget_sentiment_classifier_config", "ngram range:", None))
        self.label_17.setText(_translate("widget_sentiment_classifier_config", "max df:", None))
        self.label_18.setText(_translate("widget_sentiment_classifier_config", "min df:", None))
        self.label_19.setText(_translate("widget_sentiment_classifier_config", "max features: ", None))
        self.button_vectorize.setText(_translate("widget_sentiment_classifier_config", "vectorize data", None))
        self.check_use_stemming.setText(_translate("widget_sentiment_classifier_config", "use stemming", None))
        self.check_use_idf.setText(_translate("widget_sentiment_classifier_config", "use idf", None))
        self.check_binary.setText(_translate("widget_sentiment_classifier_config", "binary", None))
        self.check_remove_stopwords.setText(_translate("widget_sentiment_classifier_config", "remove stopwords", None))
        self.label_15.setText(_translate("widget_sentiment_classifier_config", "vectorizer:", None))
        self.label_20.setText(_translate("widget_sentiment_classifier_config", "features:", None))
        self.groupBox_2.setTitle(_translate("widget_sentiment_classifier_config", "Sentiment classifier", None))
        self.label_25.setText(_translate("widget_sentiment_classifier_config", "Classifier:", None))
        self.button_train.setToolTip(_translate("widget_sentiment_classifier_config", "clusterize data", None))
        self.button_train.setText(_translate("widget_sentiment_classifier_config", "train data", None))
        self.label_23.setText(_translate("widget_sentiment_classifier_config", "done in:", None))
        self.check_perform_lsa.setText(_translate("widget_sentiment_classifier_config", "perform lsa", None))
        self.label_21.setText(_translate("widget_sentiment_classifier_config", "number of components:", None))
        self.label_22.setText(_translate("widget_sentiment_classifier_config", "explained variance:", None))
        self.label_4.setText(_translate("widget_sentiment_classifier_config", "C:", None))
        self.label.setText(_translate("widget_sentiment_classifier_config", "Positive sentiment dataset", None))
        self.button_open_positive_sentiment_dataset.setToolTip(_translate("widget_sentiment_classifier_config", "open", None))
        self.button_open_positive_sentiment_dataset.setText(_translate("widget_sentiment_classifier_config", "Browse...", None))
        self.label_2.setText(_translate("widget_sentiment_classifier_config", "Negative sentiment dataset", None))
        self.button_open_negative_sentiment_dataset.setToolTip(_translate("widget_sentiment_classifier_config", "open", None))
        self.button_open_negative_sentiment_dataset.setText(_translate("widget_sentiment_classifier_config", "Browse...", None))

