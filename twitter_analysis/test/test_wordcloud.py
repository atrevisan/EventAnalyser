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
             'O rato e um mau carater',
             'A roupa do rei e legal', 
             'O rei e um rato mau',
             'A roupa e bacana', 
             'Eu gosto de batata',
             'Salve o rei da inglaterra: o rato!!',
             'Ratos trazem doencas',
             'A peste negra foi proveniente da pulga do rato, rato pulguento!!']

class TestWordcloud(unittest.TestCase):

    def test_wordcloud_generation_from_doc_list(self):

        wordcloud = WordCloud(max_words=3)
        wordcloud.generate(raw_documents=DOCUMENTS)

        self.assertGreaterEqual(3, len(wordcloud.words_))


if __name__ == '__main__':
    unittest.main()