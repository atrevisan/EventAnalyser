# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from time import time
import numpy as np
import operator

from sklearn import preprocessing
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from core.ml.dimensionality_reduction import DimensionalityReduction

class DocumentClassification:
    """Perform classification of text documents.
    
    Parameters
    ------------
    training_data : matrix[n_samples, n_features]
        Vectorized text documents used for training
        the classifier.

    training_labels : ndarray[n_samples]
        The labels from which class each training
        sample belongs to.

    test_data : matrix[n_samples, n_features]
        Vectorized text documents used for testing
        the classifier generalization capacity.

    test_labels : ndarray[n_samples]
        The labels from which class each test
        sample belongs to.

    perform_lsa : Boolean (default False)
        Reduce n_features to n_components in 
        trainning data for alghorithm speed up.

    n_components : int (default 100)
        Desired dimensionality of output data.
        Must be strictly less than the number of features. 
        The default value (2) is useful for visualisation. 
        For LSA, a value of 100 is recommended.
    """

    def __init__(self, training_data, training_labels, test_data, test_labels, perform_lsa=False, n_components=100):
        
        self.training_data = training_data
        self.training_labels = training_labels

        self.test_data = test_data
        self.test_labels = test_labels
       
        self.perform_lsa = perform_lsa

        if perform_lsa:
            self.dr = DimensionalityReduction(training_data)
            self.training_data = self.dr.perform_lsa(n_components=n_components)
            self.test_data = self.dr.transform_test_data(self.test_data)
            self.explained_variance = self.dr.explained_variance

    def multinomialNB(self):
        """Perform Multinomial Nave Bayes classification alghorithm."""

        self.classifier = "Nave Bayes"

        t0 = time()
        self.clf = MultinomialNB().fit(self.training_data, self.training_labels)
        self.classification_time = "%0.3fs" % (time() - t0)

        predicted = self.clf.predict(self.test_data)

        target_names = ['positive sentiment', 'negative sentiment']
        self.report_string = metrics.classification_report(self.test_labels, predicted, target_names=target_names)

    def linearSVC(self, C=1.0):
        """Perform SVM with linear kernel.
        
        Parameters
        ---------
        C : int
            Regularization parameter. Decreasing it if the data
            is very noisy perform regularization.

        Note
        ----
        Before training the alghorithm the training data should be
        normalized. Here we perform min-max normalization to the
        training data to normalize the features in the range [0, 1].
        """

        self.classifier = "SVM"

        self.min_max_scaler = preprocessing.MinMaxScaler()
        
        # scaled training data
        training_data = min_max_scaler.fit_transform(self.training_data)

        t0 = time()
        self.clf = LinearSVC(C=C).fit(training_data, self.training_labels)
        self.classification_time = "%0.3fs" % (time() - t0)

        test_data = self.min_max_scaler.transform(self.test_data)
        predicted = self.clf.predict(test_data)

        target_names = ['positive sentiment', 'negative sentiment']
        self.report_string = metrics.classification_report(self.test_labels, predicted, target_names=target_names)

    def predict_document_classes(self, vectorized_documents):
        """Predict class label per sample.
        
        Parameters
        ----------
        vectorized_documents : matrix[n_samples, n_features]
            Vectorized text documents which class will be predicted.
                
        return
        ------
        predicted_classes : array[n_samples]
            Predicted class label per sample.
        """

        if perform_lsa:
            vectorized_documents = self.dr.transform_test_data(vectorized_documents)

        # if svm perform feature scaling
        if self.classifier == "SVM":
            vectorized_documents = self.min_max_scaler.transform(vectorized_documents)

        predicted_classes = self.clf.predict(vectorized_documents)
        return predicted_classes


    