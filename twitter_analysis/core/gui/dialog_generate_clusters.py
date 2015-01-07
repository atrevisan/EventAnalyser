# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QDialog, QVBoxLayout, QDialogButtonBox, QLabel
from PyQt4.QtCore import Qt

from core.ml.document_clustering import DocumentClustering
from core.textutils.feature_extraction import FeatureExtractor

class GenerateClustersDialog(QDialog):
    """Perform cluster generation and show a dialog message confirming that the operation finished."""

    def __init__(self, parent = None):
        super(GenerateClustersDialog, self).__init__(parent)

        self.setWindowTitle("Generating clusters")

        layout = QVBoxLayout(self)

        # nice widget for editing the date
        self.label_generating = QLabel()
        self.label_generating.setText("Generating clusters...")
        layout.addWidget(self.label_generating)

        # OK  button
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok,
            Qt.Horizontal, self)

        layout.addWidget(self.buttons)
        self.setLayout(layout)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def clusterize_tweets(self, tweets, k):
        """Perform clusterization on the tweets.
        
        Parameters
        ----------
        tweets : list of string
            The raw documents.

        k : int
            The desired number of clusters.

        Returns
        --------
        (labels, top_words_per_cluster) : (list of int [n_samples], list of lists of string [k][max_words_per_cluster])
        """

        # extract features using a tf-idf vectorizer. Cutoff features
        # that appear in more than 60% of documents. Build a vocabulary
        # consisting of unigrams and bigrams.
        fe = FeatureExtractor(tweets, max_df=0.6, ngram_range=(1,2)) 
        X, vocabulary, feature_names = fe.tfidf_vectorizer()

        dc = DocumentClustering(X)

        dc.k_means(k)
        top_words_per_cluster = dc.get_top_words_per_cluster(feature_names)
        labels = dc.predict_cluster(tweets)
        self.label_generating.setText("Finished generating clusters")

        return (labels, top_words_per_cluster)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def generate_clusters(tweets, k, parent = None):
        """Call procedure that perform clusterization on the tweets.

        Wait for the user to hit ok on the dialog.
        
        Parameters
        ----------
        tweets : list of string
            The raw documents.

        k : int
            The desired number of clusters.

        Returns
        --------
        (labels, top_words_per_cluster) : (list of int [n_samples], list of lists of string [k][max_words_per_cluster])
        """
        dialog = GenerateClustersDialog(parent)
        
        labels, top_words_per_cluster = dialog.clusterize_tweets(tweets, k)

        result = dialog.exec_()
        
        return (labels, top_words_per_cluster, result == QDialog.Accepted)


