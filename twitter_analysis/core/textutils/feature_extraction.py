# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline

from nltk import stem

from core.textutils.text_pre_processing import get_stopwords_list

from time import time
import os

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

    use_stemming : Boolean (default False)
            Perform sufix elimination to reduce data dimensionality.

    binary : Boolean (default False)
            If True, all non-zero term counts are set to 1. 
            This does not mean outputs will have only 0/1 values, only that 
            the tf term (in case of a tfidf vectorizer) in tf-idf is binary. 
            (Set idf to False to get 0/1 outputs.)

    remove_stopwords : Boolean (default True)
            Eliminate non informative words from dataset.

    Atributes
    ----------
    analyser : function
        A callable that handles preprocessing and tokenization.
    """

    def __init__(self, raw_data, ngram_range=(1,1), max_df=0.5, min_df=2, max_features=None,
                 use_stemming=False, binary=False, remove_stopwords=True):
        
        self.raw_data = raw_data

        self.ngram_range = ngram_range

        if remove_stopwords:
            self.stop_words = STOPWORDS
        else:
            self.stop_words = []

        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features

        self.binary = binary

        if use_stemming:
            
            #print("Performing stemming...")
            t0 = time()
            stemmer = stem.RSLPStemmer()

            stemmed_tweets = []
            for tweet in self.raw_data:
                
                tweet_words = tweet.split()
                stemmed_tweet = []
                for word in tweet_words:

                    stemmed_word = stemmer.stem(word)
                    stemmed_tweet.append(stemmed_word)
                stemmed_tweets.append(" ".join(stemmed_tweet))
            
            #print("done in %fs" % (time() - t0))
            self.raw_data = stemmed_tweets

    def count_vectorizer(self):
        """Extract features using a count vectorizer.
        
        Return
        -------
        (X, vocabulary, feature_names) : (array, dict, list)
            Document term matrix, vocabulary mapping words to column indexes in X amd
            list containing words where the index from each position coresponds to a column
            in X.
        """

        #print("Extracting features from dataset using a sparse vectorizer")
        #print()

        #t0 = time()
        count_vect = CountVectorizer(ngram_range=self.ngram_range, stop_words=self.stop_words, 
                                     max_df=self.max_df, min_df=self.min_df, max_features=self.max_features,
                                     binary=self.binary) 

        
        X = count_vect.fit_transform(self.raw_data)
        

        vocabulary = count_vect.vocabulary_
        feature_names = count_vect.get_feature_names()

        self.analyser = count_vect.build_analyzer()

        #print("done in %fs" % (time() - t0))
        #print("n_samples: %d, n_features: %d" % X.shape)
        #print()
        
        return (X, vocabulary, feature_names)

    def hashing_vectorizer(self, use_idf=False):
        """Extract features using a hashing vectorizer. This vectorizer is 
        good for memory usage and speed up reasons but lacks the inverse transform,
        the mappings from words to the respective indexes in X.
        
        Return
        -------
        X : float array
            Document term matrix.
        """

        #print("Extracting features from dataset using a sparse vectorizer")
        #print()

        #t0 = time()
        if use_idf:
            # Perform an IDF normalization on the output of HashingVectorizer
            hasher = HashingVectorizer(ngram_range=self.ngram_range, stop_words=self.stop_words, 
                                       n_features=self.max_features, non_negative=True, norm=None, 
                                       binary=False)

            vectorizer = make_pipeline(hasher, TfidfTransformer())
        else:
            vectorizer = HashingVectorizer(ngram_range=self.ngram_range, stop_words=self.stop_words, 
                                           n_features=self.max_features, non_negative=False, norm='l2', 
                                           binary=False)

        
        X = vectorizer.fit_transform(self.raw_data)
        
        self.analyser = vectorizer.build_analyzer()
        
        #print("done in %fs" % (time() - t0))
        #print("n_samples: %d, n_features: %d" % X.shape)
        #print()

        return X

    def tfidf_vectorizer(self, use_idf=True):
        """Extract features using a tf-idf vectorizer.

        Parameters
        ----------
        use_idf : Boolean (default True)
            Perform inverse document frequency normalization
        
        Return
        -------
        (X, vocabulary, feature_names) : (array, dict, list)
            Document term matrix, vocabulary mapping words to column indexes in X amd
            list containing words where the index from each position coresponds to a column
            in X.
        """

        #print("Extracting features from dataset using a sparse vectorizer")
        #print()

        t0 = time()
        tfidf_vectorizer = TfidfVectorizer(ngram_range=self.ngram_range, stop_words=self.stop_words, 
                                           max_df=self.max_df, min_df=self.min_df, max_features=self.max_features,
                                           use_idf=use_idf, binary=self.binary) 

        
        X = tfidf_vectorizer.fit_transform(self.raw_data)
        

        vocabulary = tfidf_vectorizer.vocabulary_
        feature_names = tfidf_vectorizer.get_feature_names()
        
        self.analyser = tfidf_vectorizer.build_analyzer()

        #print("done in %fs" % (time() - t0))
        #print("n_samples: %d, n_features: %d" % X.shape)
        #print()

        return (X, vocabulary, feature_names)

    def get_top_ngrams(self, vocabulary, X, max_ngrams=20):
        """Get the top ngrams extracted from some dataset.

        Calculate the ngrams weight based on the sum of
        the respective tfidf or count value in the respective
        column in the document term matrix.
        
        Parameters
        ----------
        vocabulary : dict
            Dictionary mapping from words to column indexes in X.

        X : array, [n_samples, n_features]
            Bag of words model extracted from the document corpus.
            
        max_ngrams : int
            Max number of top ngrams to be retrived. 
            
        Returns
        -------
        top_ngrams : list of tuples (string, number)
            The global importance of each ngram in a text corpus in descending order. 
        """

        freqs = [(ngram, X.getcol(idx).sum()) for ngram, idx in vocabulary.items()]
        
        #sort from largest to smallest
        top_ngrams = sorted (freqs, key = lambda x: -x[1])

        if len(top_ngrams) >= max_ngrams:
            #for i, (ngram, weight) in enumerate(top_ngrams[:max_ngrams]):
            #    print ("%d: ngram: %s, weight: %s" % (i, ngram, weight))
            return top_ngrams[:max_ngrams]
        else:
            return top_ngrams