# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

from collections import OrderedDict

from core.gui.ui_widget_classification_report import Ui_widget_classification_report
from core.gui.widget_table import MyTable


class WidgetClassificationReport(QWidget, Ui_widget_classification_report):
    """This widget displays a report for the classification procedure.
    
    Parameters
    ------------
    report_string : str
        The report that will be displayed.
    """
    
    def __init__(self, report_string):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        
        self.button_ok.clicked.connect(self.close)

        report = report_string.split()

        data = OrderedDict([('', ["positive sentiment", "negative sentiment", "avg/total"]),
                            ('precision', [report[6], report[12], report[19]]), 
                            ('recall', [report[7], report[13], report[20]]), 
                            ('f1-score', [report[8], report[14], report[21]]), 
                            ('support', [report[9], report[15], report[22]])])

        self.my_table = MyTable(data, 3, 5)
        self.vlayout_table.addWidget(self.my_table)