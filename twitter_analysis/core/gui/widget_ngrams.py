# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4

import matplotlib.pyplot as plt
import os
import os.path

from core.gui.ui_widget_ngrams import Ui_widget_ngrams

class widgetNGrams(QWidget, Ui_widget_ngrams):
    """This widget displays n-grams frequency distributions.
    
    The n-grams frequency distributions are generated based on
    the hour and on the day of the week.

    Parameters
    ----------
    tweets : list of tuples
        Store tweets in the form (cluster_label, created_at, retweet_count, tweet_text).

    dataset_top_ngrams : list of tuples (string, number)
        The global importance of each ngram in a text corpus in descending order.

    file_name : string
        The file base name for the ngram that is being generated.
    """
    def __init__(self, tweets, dataset_top_ngrams, file_name):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.tweets = tweets
        self.file_name = file_name
        
        self.radio_hour.setChecked(True)
            
        self.combo_ngrams.addItems([ngram[0] for ngram in dataset_top_ngrams])
        self.combo_ngrams.activated[str].connect(self.onActivated)

    def generate_ngram_per_hour(self, file_name, ngram):
        """Generate the ngram and ngram per cluster hourly distribution graph.
        
        Parameters
        -----------
        file_name : string
            The file name for the ngram .png graph that will be generated.

        ngram : string
            The ngram from wich the hourly frequency distribution graph
            will be generated
        """

        # store the frequency of the given ngram per hour
        ngram_per_hour_frequency = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]

            tweet_tokens = tweet_text.split()
            hour = tweet_time.split()[3].split(":")[0]

            if hour in ngram_per_hour_frequency:

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_hour_frequency[hour] += 1

            else:
                ngram_per_hour_frequency[hour] = 0

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_hour_frequency[hour] += 1

                # Generate graph plot
                y = [y for x, y in sorted([(int(x), y) for x, y in list(ngram_per_hour_frequency.items())], key=lambda x : x[0])]
                x = [x for x, y in sorted([(int(x), y) for x, y in list(ngram_per_hour_frequency.items())], key=lambda x : x[0])]

                max_frequency = sorted (y, key=lambda x : -x)[0]
                #print("Max frequency: %d" %max_frequency)

                plt.plot(x, y, linewidth=1.5, label=ngram)
                plt.legend()
                plt.axis([0, 23, 0, max_frequency])
                plt.xlabel("Hour")
                plt.ylabel("N-gram frequency")
                plt.title("N-gram frequency distribution")

                plt.savefig(file_name)
                plt.close()

    def generate_ngram_per_day_of_week(self, file_name, ngram):
        """Generate the ngrams and ngrams per cluster day of week distribution graphs.
        
        Parameters
        -----------
        file_name : string
            The base name for the ngrams .png graphs that will be generated.

        ngram : string
            The ngram from wich the day of week distribution graphs
            will be generated
        """

        # store the frequency of the given ngram per day of week
        ngram_per_day_of_week_frequency = {}
        for tweet in self.tweets:

            tweet_time = tweet[1]
            tweet_text = tweet[3]

            tweet_tokens = tweet_text.split()
            day_of_week = tweet_time.split()[0]

            if day_of_week in ngram_per_day_of_week_frequency:

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_day_of_week_frequency[day_of_week] += 1

            else:
                ngram_per_day_of_week_frequency[day_of_week] = 0

                # test if the ngram is in the tweet
                if ngram in tweet_tokens:
                    ngram_per_day_of_week_frequency[day_of_week] += 1

                # Generate graph plot
                x = range(7)
                x_ticks = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

                y_values = [y for x, y in list(ngram_per_day_of_week_frequency.items())]
                x_values = [x_ticks.index(x) for x, y in list(ngram_per_day_of_week_frequency.items())]

                max_frequency = sorted (y_values, key=lambda x : -x)[0]
                
                #print("Max frequency: %d" %max_frequency)

                plt.plot(x_values, y_values, linewidth=1.5, label=ngram)
                plt.legend()
                
                plt.xticks(x, x_ticks)
                plt.ylim(0, max_frequency)
                
                plt.xlabel("Day of week")
                plt.ylabel("N-gram frequency")
                plt.title("N-gram frequency distribution")

                plt.savefig(file_name)
                plt.close()

    def onActivated(self, ngram):
        
        if self.radio_hour.isChecked():

            ngram_file_name = os.getcwd() + "\\graphs\\" + self.file_name + "_" + ngram.replace(' ', '_') + "_per_hour" + ".png"

            if not os.path.isfile(ngram_file_name):

                self.generate_ngram_per_hour(ngram_file_name, ngram)

            image = QtGui.QImage(ngram_file_name)
            pp = QtGui.QPixmap.fromImage(image.scaled(self.label_graph.width(), self.label_graph.height()))

            self.label_graph.setPixmap(pp)

        else:
            ngram_file_name = os.getcwd() + "\\graphs\\" + self.file_name + "_" + ngram.replace(' ', '_') + "_per_day_of_week" + ".png"

            if not os.path.isfile(ngram_file_name):

                self.generate_ngram_per_day_of_week(ngram_file_name, ngram)

            image = QtGui.QImage(ngram_file_name)
            pp = QtGui.QPixmap.fromImage(image.scaled(self.label_graph.width(), self.label_graph.height()))

            self.label_graph.setPixmap(pp)