# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from time import time
import pandas
import numpy as np
import operator

from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans


from core.ml.dimensionality_reduction import DimensionalityReduction

class DocumentClustering:
    """Perform a clusterization over text documents.
    
    Parameters
    ------------
    trainning_data : matrix[n_samples, n_features]
        Vectorized text documents.

    perform_lsa : Boolean (default False)
        Reduce n_samples from trainning data for alghorithm speed up.

    n_components : int (default 100)
        Desired dimensionality of output data. Must be strictly less than the number of features. 
        The default value (2) is useful for visualisation. For LSA, a value of 100 is recommended.

    Atributes
    ----------
    cluster_centers : array[k, n_features]
        Cluster centroids obtained from the clustering alghorithm.
    """

    def __init__(self, trainning_data, perform_lsa=False, n_components=100):
        
        self.trainning_data = trainning_data
        
        # Vectorizer results are normalized, which makes KMeans behave as
        # spherical k-means for better results. Since LSA/SVD results are
        # not normalized, we have to redo the normalization.
        if perform_lsa:
            dr = DimensionalityReduction(trainning_data)
            self.trainning_data = dr.performLSA(n_components=n_components)

    def k_means(self, k, use_minibatch=False):
        """Perform k-means clustering alghorithm.
        
        Parameters
        ----------
        k : int
            Desired number of clusters.

        use_minibatch : Boolean (default False)
            The MiniBatchKMeans is a variant of the KMeans algorithm which uses mini-batches 
            to reduce the computation time, while still attempting to optimise the same objective function. 
            Mini-batches are subsets of the input data, randomly sampled in each training iteration.
        """
        self.k = k

        if use_minibatch:
            self.km = MiniBatchKMeans(n_clusters=k, init='k-means++', n_init=1,
                                      init_size=1000, batch_size=1000)
        else:
            self.km = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)

        print("Clustering sparse data with %s" % self.km)
        t0 = time()
        self.km.fit(self.trainning_data)
        print("done in %0.3fs" % (time() - t0))
        print()
  
        print("Silhouette Coefficient: %0.3f" % 
              metrics.silhouette_score(self.trainning_data, self.km.labels_, metric='euclidean'))

        print()

        self.cluster_centers = self.km.cluster_centers_

    def get_top_words_per_cluster(self, feature_names, max_words_per_cluster=10):
        """Retrive the most important words from each cluster.
        
        The words importance measurement will depend on the vectorization method used.
        For example, if used a Count Vectorizer the word importance is determined by
        the respective counts for each feature in the cluster centroids.

        Parameters
        ----------
        feature_names : array of strings
            Array mapping from feature integer indexes in the trainning matrix
            to feature names.
        
        max_words_per_cluster : int (default 10)
            The desired number of most important words to be retrived from each cluster.

        Returns
        --------
        top_words_per_cluster : list of lists
            List containing k lists, each one containing max_words_per_cluster words.
        """

        order_centroids = self.cluster_centers.argsort()[:, ::-1]
        
        top_words_per_cluster = []
        
        print("Number of clusters: %d, Words per cluster: %d" %(self.k, max_words_per_cluster))
        for i in range(self.k):
            print("Cluster %d:\n" % i)
            top_words = [feature_names[ind] for ind in order_centroids[i, :max_words_per_cluster]]
            for word in top_words:
                print(' %s\n' % word, end='')
            top_words_per_cluster.append(top_words)
      
        return top_words_per_cluster

    def predict_cluster(self, raw_documents):
        """Return the index of the cluster each trainning example belongs to.

        Parameters
        ----------
        raw_documents : list of string
            The documents used to train the clustering model.
        
        Returns
        -------
        labels : array [n_samples,]
            Index of the cluster each sample belongs to.
        """

        heading = ["Documents"]
                      
        labels = self.km.predict(self.trainning_data)
        count_labels = {}
        for label in labels:
            if label in count_labels:
                count_labels[label] += 1
            else:
                count_labels[label] = 1

        lines_x = []
        lines = ["Cluster %d" % cluster for cluster in range(self.k)]
        for i, line in enumerate(lines):
            lines_x.extend([line] * count_labels[i])
        
        raw_documents = [(cluster, document) for cluster, document in zip(labels, raw_documents)]
        cluster_ordered_raw_documents = sorted(raw_documents, key=lambda x : x[0])
        cluster_ordered_raw_documents = [x[1] for x in cluster_ordered_raw_documents]
        #print (pandas.DataFrame(cluster_ordered_raw_documents, lines_x, heading))
        
        return labels