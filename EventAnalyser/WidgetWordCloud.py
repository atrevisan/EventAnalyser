from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from Ui_WidgetWordCloud import Ui_widgetWordCloud



class WidgetWordCloud(QWidget, Ui_widgetWordCloud):

    def __init__(self):

        QWidget.__init__(self)
     
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # custom event handling

    def addWordCloudToLabel(self):
        self.labelWordCloud.setText("oi")

        