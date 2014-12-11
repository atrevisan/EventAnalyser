from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from Ui_FetchTweets import Ui_fetchTweetsObject
from time import sleep
from TwyithonParams import *
from TextUtils import preProcessTweetText
import csv
import pickle
import re

class FetchTweets(QWidget, Ui_fetchTweetsObject):

    def __init__(self, parentWindow):

        QWidget.__init__(self)
 
        self.parentWindow = parentWindow

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # custom event handling
        self.pushButtonSearch.clicked.connect(self.fetchTweets)
        self.pushButtonStopSearching.clicked.connect(self.stopFetchingTweets)
        self.lineEditOutputFile.textChanged.connect(self.outputFileSupplied)
        
        self._active = False
        self.pushButtonSearch.setEnabled(False)
        self.pushButtonStopSearching.setEnabled(False)


    def outputFileSupplied(self, string):
        self.outputFileName = string
        self.pushButtonSearch.setEnabled(True)

    def fetchTweets(self):
        if not self._active:
            self._active = True
           
            self.pushButtonSearch.setEnabled(False)
            self.pushButtonStopSearching.setEnabled(True)
            self.parentWindow.statusBar().setStyleSheet("")
            self.parentWindow.statusBar().showMessage("")

            QtCore.QTimer.singleShot(0, self.askTwitter)
        else:
            self._active = False

    def closeEvent(self, event):
       self._active = False

    def addHashTags(self, hashTags, hashTagsList):

        for hashTag in hashTagsList:

            hashTag = hashTag.lower()
            if hashTag in hashTags:
                hashTags[hashTag] += 1
            else:
                hashTags[hashTag] = 1


    def askTwitter(self):

        querry = self.lineEditQuerry.text()

        api = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        tweets = []
        hashTags = {}
     
        csvFile = open("tweets/" + self.outputFileName + ".csv", 'w', encoding='utf8', newline='')
        csvWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        i = 0
        tweetsCount = 0

        try:
            while self._active:

                #----------------------------------------------------------------#
                # STEP 1: Query Twitter
                # STEP 2: Save the returned tweets
                # STEP 3: Get the next max_id
                #----------------------------------------------------------------#

                # STEP 1: Query Twitter
                if(0 == i):

                    # Query twitter for data. 
                    results = api.search(q=querry, count='100', lang='pt')
            
                else:
                    # After the first call we should have max_id from result of previous call. Pass it in query.
                    results = api.search(q=querry, include_entities='true', max_id=next_max_id, lang='pt')

                # STEP 2: Save the returned tweets
                for result in results['statuses']:

                    tweet_text = result['text']
                    hashTagsList = re.findall(r"#([^\s]+)", tweet_text)
                    if len(hashTagsList):
                        self.addHashTags(hashTags, hashTagsList)

                    tweet_text = preProcessTweetText (result['text'])
                    created_at = result["created_at"]
                    retweet_count = result["retweet_count"]
            
                    if not tweet_text in tweets:
                        tweets.append(tweet_text)
                        csvWriter.writerow(['|'+str(created_at)+'|', '|'+str(retweet_count)+'|', '|'+tweet_text+'|'])
                        tweetsCount += 1
                        sleep(0.05)
                        self.lineEditTweetsCount.setText(str(tweetsCount))
                        QtGui.qApp.processEvents()

                        if not self._active:
                            break
                        
                # STEP 3: Get the next max_id
                try:
                    # Parse the data returned to get max_id to be passed in consequent call.
                    next_results_url_params = results['search_metadata']['next_results']
                    next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
                except:
                    
                    sleep(60 * 15)
                    continue
                    
                i += 1

        finally:
            
            csvFile.close()
            with open("tweets/" + self.outputFileName + "HashTags.txt", 'wb') as handle:
                pickle.dump(hashTags, handle)
            #json.dump(hashTags, open("tweets/" + self.outputFileName + "HashTags.txt", 'w'))

    def stopFetchingTweets(self):
        if self._active:
            self._active = False
            self.pushButtonStopSearching.setEnabled(False)
            self.parentWindow.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.parentWindow.statusBar().showMessage("Finished loading tweets")