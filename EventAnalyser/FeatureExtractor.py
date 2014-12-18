
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline

from time import time


class FeatureExtractor:

    def __init__(self, dataset, useIDF=True, useHashing=False, maxNumberOfFeatures=10000, ngramRange=(1,2)):
        '''
        Extract features using the bag-of-words model and a sparse vectorizer

        dataset: set of text documents from witch numerical features will be extracted
        useIDF: Enable/Disable Inverse Document Frequency feature weighting
        useHashing: Use a hashing feature vectorizer
        maxNumberOfFeatures: Maximum number of features (dimensions) to extract from text data
        '''

        # list of stopwords in portuguese language
        stopwords = self.getStopWordList("stopwords.txt")

        print("Extracting features from the training dataset using a sparse vectorizer")
        t0 = time()
        if useHashing:
            if useIDF:
                # Perform an IDF normalization on the output of HashingVectorizer
                hasher = HashingVectorizer(n_features=maxNumberOfFeatures,
                                           stop_words=stopwords, 
                                           non_negative=True,
                                           norm=None, 
                                           binary=False,
                                           ngram_range=ngramRange)
                vectorizer = make_pipeline(hasher, TfidfTransformer())
            else:
                vectorizer = HashingVectorizer(n_features=maxNumberOfFeatures,
                                               stop_words=stopwords,
                                               non_negative=False, 
                                               norm='l2',
                                               binary=False,
                                               ngram_range=ngramRange)
        else:
            vectorizer = TfidfVectorizer(max_df=0.5, 
                                         max_features=maxNumberOfFeatures,
                                         min_df=2, 
                                         stop_words=stopwords,
                                         use_idf=useIDF,
                                         ngram_range=ngramRange)

        self.vectorizer = vectorizer
        self.trainingSet = self.vectorizer.fit_transform(dataset)

        print("done in %fs" % (time() - t0))
        print("n_samples: %d, n_features: %d" % self.trainingSet.shape)
        print()

    def getStopWordList(self, stopWordListFileName):
        #read the stopwords
        stopWords = []
        stopWords.append('at_user')
        stopWords.append('url')
        stopWords.append('rt')

        fp = open(stopWordListFileName, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
        return stopWords
    #end

    def getVocabulary(self):
        return self.vectorizer.get_feature_names()




