# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4

import matplotlib.pyplot as plt
import os

from core.gui.ui_widget_ngrams import Ui_widget_ngrams
from core.textutils.feature_extraction import FeatureExtractor

class widgetNGrams(QWidget, Ui_widget_ngrams):
    """This widget displays n-grams frequency distributions.
    
    The n-grams frequency distributions are generated based on
    the hour and on the day of the week.

    Parameters
    ----------
    tweets : list of tuples
        Store tweets in the form (created_at, retweet_count, tweet_text).

    file_name : string
        The file name for the wordcloud that is being generated.

    regenerate_files : list
        Contain file names that need to be regenarated in case a new dataset is selected.

    Atributes
    ----------
    analyser : function
        A callable that handles preprocessing and tokenization.
    """
    def __init__(self, tweets, file_name, regenerate_files):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.file_name = file_name
        self.tweets = tweets
        self.regenerate_files = regenerate_files
        self.radio_hour.setChecked(True)

        tweets_text = [tweet[2] for tweet in tweets]

        # extract the top n-grams from the dataset
        fe = FeatureExtractor(tweets_text, ngram_range=(1,2), max_features=20)
        X, vocabulary, feature_names = fe.count_vectorizer()
        top_ngrams = fe.get_top_words(vocabulary, X, max_words=20)
    
        self.analyser = fe.analyser
            
        self.combo_ngrams.addItems([ngram[0] for ngram in top_ngrams])
        self.combo_ngrams.activated[str].connect(self.onActivated)

    def onActivated(self, ngram):
        
        if self.radio_hour.isChecked():

            filename = os.getcwd() + "\\graphs\\" + self.file_name + ngram.replace(' ', '_') + "_per_hour" + ".png"

            if not filename in self.regenerate_files:

                # store the frequency of the chosen ngram per hour
                ngram_per_hour_frequency = {}
                for tweet in self.tweets:

                    tweet_time = tweet[0]
                    tweet_text = tweet[2]

                    tweet_tokens = self.analyser(tweet_text)
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

                plt.savefig(filename)
                plt.close()

                self.regenerate_files.append(filename)

            image = QtGui.QImage(filename)
            pp = QtGui.QPixmap.fromImage(image.scaled(self.label_graph.width(), self.label_graph.height()))

            self.label_graph.setPixmap(pp)