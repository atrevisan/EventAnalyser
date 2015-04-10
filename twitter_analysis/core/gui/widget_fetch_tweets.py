# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore

from core.gui.ui_widget_fetch_tweets import Ui_widget_fetch_tweets
from core.textutils.text_pre_processing import pre_process_tweet_text

from twython import Twython
from time import sleep
from time import time

import csv
import pickle
import re
import os

class WidgetFetchTweets(QWidget, Ui_widget_fetch_tweets):
    """This widget contain gui elements for fetching tweets that correspond to a given search querry.
            
    Parameters
    ----------
    main_window : MainWindow
        A reference for the application main window so it can change the status bar.

    Atributes
    -------
    _active : Boolean
        It keeps the fetching process state.

    hashtags : dict
        map hashtags to frequencies.

    tweets : list of tuples
        store tweets in the form (created_at, retweet_count, tweet_text).
    """
    def __init__(self, main_window):

        QWidget.__init__(self)
 
        self.main_window = main_window

        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # for some reason not loading icons correctly inside designer
        self.button_save_tweets.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\save.png")))
        self.button_fetch_tweets.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\mg.png")))
        self.button_stop_fetching.setIcon(QtGui.QIcon(QtGui.QPixmap(os.getcwd() + r"\core\gui\assets\stop.png")))

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

    def add_hashtags(self, hashtags_list):
        """Add hashtags from a given tweet to a dict mapping hashtags to frequencies.
           
        Parameters
        ----------
        hashtags_list : list
            hashtags from a given tweet
        """

        for hashtag in hashtags_list:

            hashtag = hashtag.lower()
            if hashtag in self.hashtags:
                self.hashtags[hashtag] += 1
            else:
                self.hashtags[hashtag] = 1


    def ask_twitter(self):
        """It fetches the tweets that correspond to a given search querry supplied by the user.
        
        It uses the Twithon api for fetching tweets. The tweets are fetched in a paginated fashion.
        Calls the pre_process_tweet_text() and add_hashtags() functions.
        
        Parameters
        ----------
        self
        """

        querry = self.line_edit_querry.text()

        # get twitter developer key and access token, they are required for buiulding 
        # an application that access twitter data
        with open(os.getcwd() + '\\core\\gui\\twithon_params.txt', 'rb') as handle:
            twithon_params = pickle.loads(handle.read())
        
        api = Twython(twithon_params['APP_KEY'], access_token=twithon_params['ACCESS_TOKEN'])
        
        self.tweets = []
        tweet_text_list = []
        self.hashtags = {}
     
        i = 0
        tweet_count = 0

        # max of 180 querries per 15 minutes
        QUERY_PER_SEC = 15*60/180.0  
        last_update = 0
        try:
            while self._active:

                #----------------------------------------------------------------#
                # STEP 1: Query Twitter
                # STEP 2: Save the returned tweets
                # STEP 3: Get the next max_id
                #----------------------------------------------------------------#

                tdiff = time() - last_update
                if tdiff < QUERY_PER_SEC:
                    sleep(QUERY_PER_SEC - tdiff) 
                
                last_update = time()

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
                        self.add_hashtags(hashtags_list)

                    tweet_text = pre_process_tweet_text(result['text'])
                    created_at = result["created_at"]
                    retweet_count = result["retweet_count"]
            
                    if not tweet_text in tweet_text_list:
                        
                        tweet_text_list.append(tweet_text)
                        tweet = (created_at, retweet_count, tweet_text)
                        self.tweets.append(tweet)

                        tweet_count += 1
                        sleep(0.05)

                        # update gui
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
                    
                    print ("Nothing to fetch")
                    sleep(60)
                    continue
                    
                i += 1

        finally:
            print ("Finish fetching")
           
    def stop_fetching(self):
        """It stops the fetching process in response for a click event and updates the status bar.
 
        Parameters
        ----------
        self
        """
        if self._active:
            self._active = False
            self.main_window.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.main_window.statusBar().showMessage("Finished fetching tweets")

    def save_tweets(self):
        """It saves the fetched tweets to the user chosen location in response for a click event.
 
        It stores the retrived tweets to a csv file in the format: (date, retweets_count, tweet_text). 
        It also stores a file containing hashtag counts in a dict format.

        Parameters
        ----------
        self
        """
             
        file_name = QtGui.QFileDialog.getSaveFileName(self, "Save data", os.getcwd() + "\\tweets\\", "*.csv")

        # Case the user select an already existent file
        if file_name.find(".csv") != -1:
            file_name = file_name[:-4]

        csv_file = open(file_name + ".csv", 'w', newline='', encoding="utf-8")
        csv_writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        for tweet in self.tweets:
            csv_writer.writerow(['|'+str(tweet[0])+'|', '|'+str(tweet[1])+'|', '|'+tweet[2]+'|'])
        csv_file.close()
           
        with open(file_name + "_hashtags.txt", 'wb') as handle:
            pickle.dump(self.hashtags, handle)