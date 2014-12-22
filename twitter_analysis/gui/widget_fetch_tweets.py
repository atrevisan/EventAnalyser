# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
from gui.ui_widget_fetch_tweets import Ui_widget_fetch_tweets
from twython import Twython
from time import sleep
from textutils.text_pre_processing import pre_process_tweet_text 

import csv
import pickle
import re

class WidgetFetchTweets(QWidget, Ui_widget_fetch_tweets):
    """Widget fetch tweets that correspond to a given search querry from Twitter.
            
    Parameters
    ----------
    main_window : MainWindow
        A reference for the application main window so it cans change the status bar.

    Atributes
    -------
    _active : Boolean
        It keeps the fetching process state.
    """
    def __init__(self, main_window):

        QWidget.__init__(self)
 
        self.main_window = main_window

        # set up User Interface (widgets, layout...)
        self.setupUi(self)
        self.button_save_tweets.setIcon(QtGui.QIcon(QtGui.QPixmap("gui\Save.png")))

        # custom event handling
        self.button_fetch_tweets.clicked.connect(self.fetch_tweets)
        self.button_stop_fetching.clicked.connect(self.stop_fetching)
        self.button_save_tweets.clicked.connect(self.save_tweets)
      
        self._active = False    

    def fetch_tweets(self):
        """Start the fetching Twitter process so that it is possible to update the gui dinamically.
        
        It will call the ask_twitter() function that will run in a separate thread.
        """

        if not self._active:
            self._active = True

            self.main_window.statusBar().setStyleSheet("")
            self.main_window.statusBar().showMessage("")

            QtCore.QTimer.singleShot(0, self.ask_twitter)
        else:
            self._active = False

    def closeEvent(self, event):
       self._active = False

    def add_hashtags(self, hashtags, hashtags_list):
        """Add hashtags from a given tweet to a dict mapping hashtags to frequencies.
           
        Parameters
        ----------
        hashtags : dict
            map hashtags to frequencies

        hashtags_list : list
            hashtags from a given tweet
        """

        for hashtag in hashtags_list:

            hashtag = hashtag.lower()
            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1


    def ask_twitter(self):
        """Widget fetch tweets that correspond to a given search querry from Twitter.
        
        It uses the Twithon api for fetching tweets and stores the retrived tweets to a csv file
        in the format: (date, retweets_count, tweet_text). It also sores a file containing hashtag
        counts.    

        Parameters
        ----------
        self
        """

        querry = self.line_edit_querry.text()

        with open('twithon_params.txt', 'rb') as handle:
            twithon_params = pickle.loads(handle.read())
        
        api = Twython(twithon_params['APP_KEY'], access_token=twithon_params['ACCESS_TOKEN'])
        
        self.tweets = []
        tweet_text_list = []
        hashtags = {}
     
        #csvFile = open("tweets/" + self.outputFileName + ".csv", 'w', encoding='utf8', newline='')
        #csvWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        i = 0
        tweet_count = 0

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
                    hashtags_list = re.findall(r"#([^\s]+)", tweet_text)

                    if len(hashtags_list):
                        self.add_hashtags(hashtags, hashtags_list)

                    tweet_text = pre_process_tweet_text(result['text'])
                    created_at = result["created_at"]
                    retweet_count = result["retweet_count"]
            
                    tweet = (created_at, retweet_count, tweet_text)

                    if not tweet_text in tweet_text_list:
                        self.tweets.append(tweet)
                        #csvWriter.writerow(['|'+str(created_at)+'|', '|'+str(retweet_count)+'|', '|'+tweet_text+'|'])
                        tweet_count += 1
                        sleep(0.05)
                        self.line_edit_tweet_count.setText(str(tweet_count))
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
            pass
            #csvFile.close()
            #with open("tweets/" + self.outputFileName + "HashTags.txt", 'wb') as handle:
            #    pickle.dump(hashTags, handle)
            ##json.dump(hashTags, open("tweets/" + self.outputFileName + "HashTags.txt", 'w'))

    def stop_fetching(self):
        if self._active:
            self._active = False
            self.main_window.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.main_window.statusBar().showMessage("Finished fetching tweets")

    def save_tweets(self):
        
        file_name = QtGui.QFileDialog.getSaveFileName(self, "Save data", "tweets/", "*.csv")
        print(file_name)