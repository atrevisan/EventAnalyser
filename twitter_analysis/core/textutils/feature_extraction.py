
from sklearn.feature_extraction.text import CountVectorizer

from time import time
import os

from core.textutils.text_pre_processing import get_stopwords_list

STOPWORDS = get_stopwords_list(os.getcwd() + r"\core\textutils\stopwords.txt")

class FeatureExtractor:
    """This class encapsulate the functionalities from sklearn vectorizers.
    
    It uses one of the sklearn.feature_extraction.text vectorizers (count, tfidf, hash, ...)
    to convert a collection of text documents to a matrix of features. 

    Parameters
    -----------
    raw_data : list
        A list of documents, each document is represented by a string.

    ngram_range : tuple (default (1, 1))
        The lower and upper boundary of the range of n-values for different n-grams to be extracted.

    stop_words : list (deafult None)
        List of words that will be discarded from the fitted vocabulary.

    max_df : float in range [0.0, 1.0] or int, optional, (default 0.5)
        When building the vocabulary ignore terms that have a document frequency strictly higher than 
        the given threshold (corpus-specific stop words). If float, the parameter represents a proportion 
        of documents, integer absolute counts.

    min_df :  float in range [0.0, 1.0] or int, optional, (default 2)
        When building the vocabulary ignore terms that have a document frequency strictly lower than the
        given threshold. This value is also called cut-off in the literature. If float, the parameter represents 
        a proportion of documents, integer absolute counts.

    max_features : int (default None)
        If not None, build a vocabulary that only consider the top max_features ordered by term frequency across 
        the corpus.
    """

    def __init__(self, raw_data, ngram_range=(1,1), stop_words=None, max_df=0.5, min_df=2, max_features=None):
        
        self.raw_data = raw_data

        self.ngram_range = ngram_range

        if stop_words is None:
            self.stop_words = STOPWORDS

        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features

    def count_vectorizer(self):
        """Extract features using a count vectorizer.
        
        Return
        -------
        (X, vocabulary) : (array, dict)
            Document term matrix and vocabulary (mapping words to column indexes in X).
        """

        print("Extracting features from dataset using a sparse vectorizer")
        print()

        t0 = time()
        count_vect = CountVectorizer(ngram_range=self.ngram_range, stop_words=self.stop_words, 
                                     max_df=self.max_df, min_df=self.min_df, max_features=self.max_features) 

        self.X = count_vect.fit_transform(self.raw_data)
        self.vocabulary = count_vect.vocabulary_

        print("done in %fs" % (time() - t0))
        print("n_samples: %d, n_features: %d" % self.X.shape)
        print()

        return (self.X, self.vocabulary)

    def get_top_words(self, vocabulary, doc_term_matrix, number_of_terms=20):
        """Get top terms extracted from some dataset.
        
        Parameters
        ----------
        vocabulary : dict
            Dictionary mapping to counts or tf-idf.

        doc_term_matrix : array, [n_samples, n_features]
            Bag of words model extracted from a document corpus. 
            
        Returns
        -------
        top_terms : list of tuples (word, weight)
            The global importance of each word in a text corpus in descending order. 
        """

        freqs = [(word, doc_term_matrix.getcol(idx).sum()) for word, idx in vocabulary.items()]
        
        #sort from largest to smallest
        top_terms = sorted (freqs, key = lambda x: -x[1])

        for i, (term, weight) in enumerate(top_terms[:number_of_terms]):
            print ("%d: word: %s, weight: %s" % (i, term, weight))

        return top_terms[:number_of_terms]