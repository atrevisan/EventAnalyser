# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fetch_tweets.ui'
#
# Created: Tue Nov 18 09:34:36 2014
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

class Ui_fetchTweetsObject(QtGui.QWidget):

    def __init__(self, mainWindow):
        super(Ui_fetchTweetsObject, self).__init__()
        self.mainWindow = mainWindow
        self.setupUi(self)

    def setupUi(self, fetchTweetsObject):
        fetchTweetsObject.setObjectName(_fromUtf8("fetchTweetsObject"))
        fetchTweetsObject.resize(800, 400)
        self.verticalLayout_2 = QtGui.QVBoxLayout(fetchTweetsObject)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit = QtGui.QLineEdit(fetchTweetsObject)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lineEdit)
        self.pushButton = QtGui.QPushButton(fetchTweetsObject)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("gui\\mg.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.lineEdit_2 = QtGui.QLineEdit(fetchTweetsObject)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lineEdit_2)
        self.pushButton_2 = QtGui.QPushButton(fetchTweetsObject)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("gui\\stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(fetchTweetsObject)
        QtCore.QMetaObject.connectSlotsByName(fetchTweetsObject)

        self.pushButton.clicked.connect(self.fetchTweets)
        self.pushButton_2.clicked.connect(self.stopFetchingTweets)

    def fetchTweets(self):
        print("oioi")
        

    def stopFetchingTweets(self):
        self.mainWindow.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
        self.mainWindow.statusBar().showMessage("Finished loading tweets")

    def retranslateUi(self, fetchTweetsObject):
        fetchTweetsObject.setWindowTitle(_translate("fetchTweetsObject", "Fetch Tweets", None))

