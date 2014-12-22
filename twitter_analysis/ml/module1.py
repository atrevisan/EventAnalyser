from FeatureExtractor import FeatureExtractor
from MachineLearning import Clustering

import csv

dataSet = []
with open('tweets/protesto.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='|')
    for row in reader:
        dataSet.append(row[2])

extractor = FeatureExtractor(dataSet)
trainingSet = extractor.trainingSet

clustering = Clustering(trainingSet)
clustering.clusterizeDocuments(5)
topTermsPerCluster = clustering.getTopTermsPerCluster(extractor.getVocabulary())
