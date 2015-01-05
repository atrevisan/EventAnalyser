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

from core.ml.document_clustering import DocumentClustering
from core.textutils.feature_extraction import FeatureExtractor

DOCUMENTS = ['O rato roeu a roupa do rei de roma',
             'O rato e um mau carater',
             'A roupa do rei e legal', 
             'O rei e um rato mau',
             'A roupa e bacana', 
             'Eu gosto de batata',
             'Salve o rei da inglaterra: o rato!!',
             'Ratos trazem doencas',
             'A peste negra foi proveniente da pulga do rato, rato pulguento!!',
             'Batata e bom',
             'Eu gosto de estudar e batata',
             'Batata e um turbeculo',
             'Sera que a batata e uma raiz ?',
             'Tem gente que nao gosta de batata',
             'Batata frita e muito bom']

class TestDocumentClustering(unittest.TestCase):

    def test_document_clustering(self):

        fe = FeatureExtractor(DOCUMENTS, max_df=0.6, ngram_range=(1,1)) 
        X, vocabulary, feature_names = fe.tfidf_vectorizer()

        dc = DocumentClustering(X)
        dc.k_means(2)
        top_words_per_cluster = dc.get_top_words_per_cluster(feature_names)
 
        self.assertEqual(len(top_words_per_cluster), 2)

    def test_predic_cluster(self):

        fe = FeatureExtractor(DOCUMENTS, min_df=0, ngram_range=(1,2), max_features=30) 
        X, vocabulary, feature_names = fe.tfidf_vectorizer()

        dc = DocumentClustering(X)
        dc.k_means(2)

        dc.get_top_words_per_cluster(feature_names)
        lines, columns = X.shape
        labels = dc.predict_cluster(DOCUMENTS)

        self.assertEqual(lines, len(labels))
        

if __name__ == '__main__':
    unittest.main()