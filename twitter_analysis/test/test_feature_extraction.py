# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import unittest
import os
import numpy as np

import sys
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from core.textutils.feature_extraction import FeatureExtractor

DOCUMENTS = ['O rato roeu a roupa do rei de roma',
             'O rato é um mau carater',
             'A roupa do rei é legal', 
             'O rei é um rato mau',
             'A roupa é bacana', 
             'Eu gosto de batata',
             'Salve o rei da inglaterra: o rato!!',
             'Ratos trazem doenças',
             'A peste negra é proveniente da pulga do rato, rato pulguento!!']

class TestFeatureExtraction(unittest.TestCase):

    def test_count_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS, max_features=3)
        X, vocabulary = fe.count_vectorizer()
        lines, columns = X.shape
        self.assertGreaterEqual(3, columns)

    def test_hashing_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS, max_features=3)
        X = fe.hashing_vectorizer()
        lines, columns = X.shape
        self.assertGreaterEqual(3, columns)

    def test_tfidf_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS)

        # the most common word rato should not
        # be present in more than 50% of the documents
        X, vocabulary = fe.tfidf_vectorizer()
    
        self.assertNotIn("rato", vocabulary.keys())
    

    def test_get_top_words(self):

        fe = FeatureExtractor(DOCUMENTS)
        X, vocabulary = fe.count_vectorizer()
        top_words = fe.get_top_words(vocabulary, X, max_words=6)
        self.assertGreaterEqual(6, len(top_words))

if __name__ == '__main__':
    unittest.main()