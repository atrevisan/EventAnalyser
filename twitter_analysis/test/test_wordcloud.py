# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import unittest
import os

import sys
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from core.textutils.wordcloud import WordCloud

DOCUMENTS = ['O rato roeu a roupa do rei de roma',
             'O rato é um mau carater',
             'A roupa do rei é legal', 
             'O rei é um cara mau',
             'A roupa é bacana', 
             'Eu gosto de batata',
             'Salve o rei da inglaterra!!',
             'Ratos trazem doenças',
             'A peste negra é proveniente da pulga do rato']

class TestWordcloud(unittest.TestCase):

    def test_wordcloud_generation_from_doc_list(self):

        wordcloud = WordCloud(max_words=3)
        wordcloud.generate(raw_documents=DOCUMENTS)

        self.assertGreaterEqual(3, len(wordcloud.words_))


if __name__ == '__main__':
    unittest.main()