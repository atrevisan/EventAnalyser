# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCursor
from PyQt4.QtGui import QMessageBox

import os
import numpy as np
import csv
import pickle
import itertools
import matplotlib.pyplot as plt
                                         
from core.gui.ui_widget_ml_config import Ui_widget_ml_config
from core.textutils.feature_extraction import FeatureExtractor
from core.ml.document_clustering import DocumentClustering
from core.textutils.wordcloud import WordCloud
from core.textutils.text_pre_processing import get_stopwords_list

class WidgetMLConfig(QWidget, Ui_widget_ml_config):
    """This widget displays a range of options for clustering and classification tasks configuration.

    Atributes
    -------
    tweets : list of tuples
        Store tweets in the form (created_at, retweet_count, tweet_text).

    hashtags : dict
        Map hashtags to frequencies.

    dataset_top_ngrams : list of tuples (string, number)
        The global importance of each ngram in a text corpus in descending order. 

    top_ngrams_per_cluster : list of lists of tuples (string, number)
        List containing k lists, each one containing max_ngrams_per_cluster tuples
        (ngram, weight), where weight is the centroid component value.

    cluster_labels : array [n_samples,]
        Index of the cluster each sample belongs to.
    """
    def __init__(self):

        QWidget.__init__(self)

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.group_clustering.setDisabled(True)

        self.button_open_file.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\open.png")))
        self.button_save_clustering_config.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\save.png")))

        self.combo_vectorizer_clustering.addItems(["tfidf vectorizer", "count vectorizer"])
        self.combo_ngram_range_clustering.addItems(["(1,1)", "(1,2)", "(1,3)", "(2,2)", "(2,3)", "(3,3)"])
        self.combo_max_df_clustering.addItems(["%.1f" % number for number in list(np.arange(0.0, 1.1, 0.1))] + [str(number) for number in list(range(1, 10001))]) 
        self.combo_min_df_clustering.addItems(["%.1f" % number for number in list(np.arange(0.0, 1.1, 0.1))] + [str(number) for number in list(range(1, 10001))])
        self.combo_max_features_clustering.addItems([str(num) for num in list(range(2, 10001))])
        self.combo_clusters.addItems([str(num) for num in list(range(2, 11))])
        self.combo_n_components_clustering.addItems([str(num) for num in list(range(2, 500))])

        self.combo_ngram_range_clustering.setCurrentIndex(1)
        self.combo_max_df_clustering.setCurrentIndex(5)
        self.combo_min_df_clustering.setCurrentIndex(1)
        self.combo_max_features_clustering.setCurrentIndex(498)
        self.combo_clusters.setCurrentIndex(3)
        self.combo_n_components_clustering.setCurrentIndex(98)

        self.check_use_idf_clustering.setChecked(True)
        self.check_remove_stopwords_clustering.setChecked(True)

        self.combo_n_components_clustering.setDisabled(True)

        self.combo_vectorizer_clustering.activated[str].connect(self.on_activated_combo_vectorizer_clustering)
        self.combo_max_features_clustering.activated[int].connect(self.on_activated_combo_max_features_clustering)

        self.check_perform_lsa_clustering.stateChanged.connect(self.check_lsa_state_changed)
        self.button_clusterize.clicked.connect(self.start_clustering)
        self.button_open_file.clicked.connect(self.open_tweets_file)
        self.button_save_clustering_config.clicked.connect(self.save_clusterized_data)

    def open_tweets_file(self):
        """Open a csv file containing Twitter text data that will be analysed in response of a click event.

        Calculate also the percentage of stopwords in the corpus and the corpus lexical
        diversity.
        
        Notes
        -------
        Each csv file has also a binary file associated that contains hashtags
        stored in a dict format.
        """
            
        # user chosen file 
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open data", os.getcwd() + "\\tweets\\", "*.csv")
        
        self.tweets = []
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                self.tweets.append((tweet[0], tweet[1], tweet[2]))

        # loading hashtags
        with open(file_name[:-4] + "_hashtags.txt", 'rb') as handle:
            self.hashtags = pickle.loads(handle.read())

        self.group_clustering.setDisabled(False)

        tweets = [tweet[2] for tweet in self.tweets]

        tweets_text = ' '.join(tweet)
        
        # calculate lexical diversity
        lexical_diversity = len(tweets_text) / len(set(tweets_text))

        # calculate percentage of stopwords
        stopwords = get_stopwords_list(os.getcwd() + r"\core\textutils\stopwords.txt")
        stopwords_count = sum([tweets_text.count(stopword) for stopword in stopwords])
        percentage_of_stopwords = 100 * stopwords_count / len(tweets_text)

        self.label_lexical_diversity.setText("%.2f" % float(lexical_diversity))
        self.label_percentage_stopwords.setText("%.2f%%" % float(percentage_of_stopwords))


    def start_clustering(self):
        """Perform the clustering procedure."""

        # Clusterization parameters
        k = list(range(2, 11))[self.combo_clusters.currentIndex()]
        vectorizer = self.combo_vectorizer_clustering.currentText()
        ngram_range = [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)][self.combo_ngram_range_clustering.currentIndex()]
        max_df = list(itertools.chain([number for number in list(np.arange(0.0, 1.1, 0.1))], list(range(1, 10001))))[self.combo_max_df_clustering.currentIndex()]
        min_df = list(itertools.chain([number for number in list(np.arange(0.0, 1.1, 0.1))], list(range(1, 10001))))[self.combo_min_df_clustering.currentIndex()]
        max_features = list(range(2, 10001))[self.combo_max_features_clustering.currentIndex()]
        use_idf = not self.check_use_idf_clustering is None and self.check_use_idf_clustering.isChecked()
        use_stemming = self.check_use_stemming_clustering.isChecked()
        binary = self.check_binary_clustering.isChecked()
        remove_stopwords = self.check_remove_stopwords_clustering.isChecked()
        use_minibatch = self.check_use_minibatch_clustering.isChecked()
        perform_lsa = self.check_perform_lsa_clustering.isChecked()
        n_components = list(range(2, max_features))[self.combo_n_components_clustering.currentIndex()]


        tweets = [tweet[2] for tweet in self.tweets]
      
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        fe = FeatureExtractor(tweets, 
                              max_df=max_df, 
                              min_df=min_df,
                              max_features=max_features, 
                              ngram_range=ngram_range, 
                              use_stemming=use_stemming,
                              binary=binary,
                              remove_stopwords=remove_stopwords) 

        try:
            if vectorizer == "tfidf vectorizer":

                X, vocabulary, feature_names = fe.tfidf_vectorizer(use_idf=use_idf)

            else:
                X, vocabulary, feature_names = fe.count_vectorizer()

            self.dataset_top_ngrams = fe.get_top_ngrams(vocabulary, X)
            
            dc = DocumentClustering(X, perform_lsa=perform_lsa, n_components=n_components)

            if use_minibatch:
                dc.k_means(k, use_minibatch=use_minibatch)
            else:
                dc.k_means(k)

            self.top_ngrams_per_cluster = dc.get_top_ngrams_per_cluster(feature_names)
            self.cluster_labels = dc.predict_clusters()
            
            n_features = dc.trainning_data.shape[1]
            clusterization_time = dc.clusterization_time
            silhuette_coefficient = dc.silhuette_coefficient
        
            self.label_donein_clustering.setText(clusterization_time)
            self.label_silhuette.setText(silhuette_coefficient)
            self.label_features_clustering.setText(str(n_features))

            if perform_lsa:
                self.label_explained_variance.setText(str(dc.explained_variance) + "%")
        
        except ValueError:
            
            QMessageBox.about(self, "Error", "Problem while extracting features")

        QApplication.restoreOverrideCursor()
      
    def generate_wordclouds(self, file_name):
        """Generate wordcloud and wordcloud per cluster for the clusterized dataset.
        
        Parameters
        -----------
        file_name : string
            The base name for the wordclouds .png file names.
        """ 

        wordcloud_filename = os.getcwd() + "\\wordclouds\\" + file_name + ".png"

        wordcloud = WordCloud(max_words=20, prefer_horizontal=0.80).generate(top_ngrams=self.dataset_top_ngrams)
        wordcloud.to_file(wordcloud_filename)

        # Generate wordcloud per cluster
        for cluster_label, cluster_ngrams in enumerate(self.top_ngrams_per_cluster):
            
            wordcloud = WordCloud(max_words=20, prefer_horizontal=0.80).generate(top_ngrams=cluster_ngrams)
            wordcloud.to_file(wordcloud_filename[:-4] + "_cluster_" + str(cluster_label) + ".png")

    

    

    def generate_ngrams(self, file_name):
        """Generate the ngrams and ngrams per cluster for the clusterized dataset.
        
        Parameters
        -----------
        file_name : string
            The base name for the ngrams .png graphs that will be generated.
        """

        # first ngrams per hour
        for ngram in self.dataset_top_ngrams:

            ngram_filename = os.getcwd() + "\\graphs\\" + file_name + "_" + ngram[0].replace(' ', '_') + "_per_hour" + ".png"
            self.generate_ngram_per_hour(ngram_filename, ngram[0])

        # ngrams per cluster
        for cluster_label, cluster_top_ngrams in enumerate(self.top_ngrams_per_cluster):

            for ngram in cluster_top_ngrams:

                ngram_filename = os.getcwd() + "\\graphs\\" + file_name + "_" + ngram[0].replace(' ', '_') +  "_per_hour_" + "cluster_" + str(cluster_label) + ".png"
                self.generate_ngram_per_hour(ngram_filename, ngram[0])
        
        # second ngram per day of week
        for ngram in self.dataset_top_ngrams:

            ngram_filename = os.getcwd() + "\\graphs\\" + file_name + "_" + ngram[0].replace(' ', '_') + "_per_day_of_week" + ".png"
            self.generate_ngram_per_day_of_week(ngram_filename, ngram[0])

        # ngrams per cluster
        for cluster_label, cluster_top_ngrams in enumerate(self.top_ngrams_per_cluster):

            for ngram in cluster_top_ngrams:

                ngram_filename = os.getcwd() + "\\graphs\\" + file_name + "_" + ngram[0].replace(' ', '_') +  "_per_day_of_week_" + "cluster_" + str(cluster_label) + ".png"
                self.generate_ngram_per_day_of_week(ngram_filename, ngram[0])

    def save_object(self, obj, filename):
        """Save objet to file.
        
        Parameters
        -----------
        obj : some object
           Object that will be saved.

        filename : str
            Filesystem path to wich the object should
            be saved.
        """
        with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    def save_clusterized_data(self):
        """Save the clustering configuration for the chosen dataset.
        
        This procedure saves the clusterized dataset the dataset top 
        ngrams, the top ngrams per cluster, the cluster labels to wich
        each tweet belongs to and the analyser function used for texttokenization. This procedure also generates 
        the wordcloud and wordclouds per cluster and save them in the file system. 
        """

        # add to the tweets to wich cluster it belongs to
        tweets = [(cluster_label, tweet_date, retweet_count, tweet_text) for cluster_label, (tweet_date, retweet_count, tweet_text) 
                                                                             in zip(self.cluster_labels, self.tweets)]
        
        file_name = QtGui.QFileDialog.getSaveFileName(self, "Save data", os.getcwd() + "\\clusterized_tweets\\", "*.csv")

        # Case the user select an already existent file
        if file_name.find(".csv") != -1:
            file_name = file_name[:-4]

        # save objects that will be used in the tweets text analysis
        self.save_object(self.dataset_top_ngrams, file_name + "_dataset_top_ngrams.pkl")
        self.save_object(self.top_ngrams_per_cluster, file_name + "_top_ngrams_per_cluster.pkl")
        #self.save_object(self.cluster_labels, file_name + "_cluster_labels.pkl")
        self.save_object(self.hashtags, file_name + "_hashtags.pkl")

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        csv_file = open(file_name + ".csv", 'w', newline='', encoding="utf-8")
        csv_writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        for tweet in tweets:
            csv_writer.writerow(['|'+str(tweet[0])+'|', '|'+str(tweet[1])+'|', '|'+str(tweet[2])+'|', '|'+tweet[3]+'|'])
        csv_file.close()

        # base file name for the wordclouds .png files that will be generated
        file_name = file_name.split("/clusterized_tweets/")[1]
        
        # Generate wordclouds
        self.generate_wordclouds(file_name)
        
        QApplication.restoreOverrideCursor()

        
    def on_activated_combo_vectorizer_clustering(self, vectorizer):

        if vectorizer == "count vectorizer" and not self.check_use_idf_clustering is None:
        
            self.vlayout_checkboxes.removeWidget(self.check_use_idf_clustering)
            self.check_use_idf_clustering.deleteLater()
            self.check_use_idf_clustering = None

        elif vectorizer == "tfidf vectorizer" and self.check_use_idf_clustering is None:
            
            self.check_use_idf_clustering = QtGui.QCheckBox()
            font = QtGui.QFont()
            font.setPointSize(10)
            self.check_use_idf_clustering.setFont(font)
            self.check_use_idf_clustering.setObjectName("check_use_idf_clustering")
            self.vlayout_checkboxes.addWidget(self.check_use_idf_clustering)
            self.check_use_idf_clustering.setText("use idf")

    def on_activated_combo_max_features_clustering(self, index):

        self.combo_n_components_clustering.clear()
        self.combo_n_components_clustering.addItems([str(num) for num in list(range(2, list(range(2, 10001))[index]))])

    def check_lsa_state_changed(self, state):

        if state == QtCore.Qt.Checked:
            self.combo_n_components_clustering.setDisabled(False)
        else:
            self.combo_n_components_clustering.setDisabled(True)