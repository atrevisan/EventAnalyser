from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans, MiniBatchKMeans

from sklearn import metrics

from time import time

class Clustering:
    def __init__(self, trainingSet, useLSA=False, nComponents=2):
        '''
        trainingSet: training data obtained from the FeatureExtractor
        useLSA: perform dimensionality reduction using latent semantic analysis (Similar to PCA) in training data
        nComponents:desired dimensionality of output data. Must be strictly less than the number of features. 
                    The default value is useful for visualisation. For LSA, a value of 100 is recommended.
        '''
        
        if useLSA:
            print("Performing dimensionality reduction using LSA")
            t0 = time()

            # Vectorizer results are normalized, which makes KMeans behave as
            # spherical k-means for better results. Since LSA/SVD results are
            # not normalized, we have to redo the normalization.
            svd = TruncatedSVD(nComponents)
            lsa = make_pipeline(svd, Normalizer(copy=False))

            self.trainingSet = lsa.fit_transform(trainingSet)

            print("done in %fs" % (time() - t0))

            explained_variance = svd.explained_variance_ratio_.sum()
            print("Explained variance of the SVD step: {}%".format(
                int(explained_variance * 100)))

            print()

        else:
            self.trainingSet = trainingSet


    def clusterizeDocuments(self, k, useMiniBatch=False, verbose=False):
        '''
        k: desired number of clusters
        useMiniBatch: Use or not ordinary k-means algorithm (in batch mode)
        verbose: Print progress reports inside k-means algorithm
        '''

        if useMiniBatch:
            self.kMeans = MiniBatchKMeans(n_clusters=k, 
                                          init='k-means++', 
                                          n_init=1,
                                          init_size=1000, 
                                          batch_size=1000, 
                                          verbose=verbose)
        else:
            self.kMeans = KMeans(n_clusters=k, 
                                 init='k-means++', 
                                 max_iter=100, 
                                 n_init=1,
                                 verbose=verbose)

        print("Clustering sparse data with %s" % self.kMeans)
        t0 = time()
        self.kMeans.fit(self.trainingSet)
        print("done in %0.3fs" % (time() - t0))
        print()

        print("Silhouette Coefficient: %0.3f" % 
              metrics.silhouette_score(self.trainingSet, self.kMeans.labels_, metric='euclidean'))
        
    def getTopTermsPerCluster(self, vocabulary, numberOfTopTerms=10):
        
        order_centroids = self.kMeans.cluster_centers_.argsort()[:, ::-1]
        k = self.kMeans.get_params()['n_clusters']

        topTermsPerCluster = []
        for i in range(k):
            
            topTerms = [vocabulary[ind] for ind in order_centroids[i, :numberOfTopTerms]]
            topTermsPerCluster.append(topTerms)

        return topTermsPerCluster