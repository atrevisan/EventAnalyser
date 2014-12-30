# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

from core.gui.ui_widget_wordcloud import Ui_widget_wordcloud

class WidgetWordcloud(QWidget, Ui_widget_wordcloud):
    """This widget contains a label for displaying a wordcloud.
    
    The wordcloud is generated based on a tf-idf vectorizer that is calculated
    from the chosen dataset.        
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # generate the wordcloud here
        #self.label_wordcloud.
