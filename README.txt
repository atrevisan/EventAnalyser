The goal of this tool is to perform intelligent information recovery over data available on Twitter 
so that it can generate summarizing information about some real world event. The tool uses machine learning
and natural language processing for achieving its goal.

The tool user from some context of interest can enter a query for collecting tweets. 
The collected tweets will be clustered and analyzed, the analyzing process generate summarization information
about the text in the messages.

The user will also enter some query for collecting training data for a sentiment classifier (SVM or Naive Bayes).
The classifier will be used against the clusterized tweets aiding in the process of generating summarization information.

You can find out more about this project on my monograph available in the root of this repository

Major instructions for running the tool. 

Using python 3.4 you should run the file main.py.

You should also download the dependency packages needed.
If in Windows a good place for download is: http://www.lfd.uci.edu/~gohlke/pythonlibs/

The main dependencies are: 

Scikit-learn
nltk
pillow
pyqt4
numpy
scipy
mathplotlib
twython -> https://github.com/ryanmcgrath/twython

You can use pip install for installing the packages.
