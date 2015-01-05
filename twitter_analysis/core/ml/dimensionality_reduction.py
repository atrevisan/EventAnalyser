# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

class DimensionalityReduction:
    """Performs dimensionality reduction over trainning data.
    
    Parameters
    -----------
    trainning_data : array [n_samples, n_features]
        Vectorized trainning data.

    Atributes
    ----------
    explained_variance : array [n_components]
        The variance of the training samples transformed by a projection to each component.
    """
    def __init__(self, trainning_data):

        self.trainning_data = trainning_data
    

    def performLSA(self, n_components=2):
        """Perform Latent semantic analysis.
        
        Parameters
        -----------
        n_components : int
            Desired dimensionality of output data. Must be strictly less than the number of features. 
            The default value is useful for visualisation. For LSA, a value of 100 is recommended.

        Returns
        ---------
        X : array [n_samples, n_components]
            reduced training data.
        """

        print("Performing dimensionality reduction using LSA")
        t0 = time()

        svd = TruncatedSVD(n_components)
        lsa = make_pipeline(svd, Normalizer(copy=False))

        X = lsa.fit_transform(trainning_data)

        print("done in %fs" % (time() - t0))

        self.explained_variance = svd.explained_variance_ratio_.sum()
        print("Explained variance of the SVD step: {}%".format(
            int(explained_variance * 100)))

        print()

        return X