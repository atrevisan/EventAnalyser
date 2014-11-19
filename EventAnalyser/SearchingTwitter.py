from twython import Twython
from TextUtils import preProcessTweetText
import csv

APP_KEY = 'SZcWKO9few3q7PWCUQJ4Tz2lZ'
APP_SECRET = 'KAN4FXH89fWcBFb7wO3iQPoYdfXrMbAcarqAWQjH3R3SGrnncM'

def fetchForTweets(countOfTweetsToBeFetched, querry, fileName):

    api = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = api.obtain_access_token()

    api = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    tweets                          =   []
     
    csvFile = open(fileName, 'w', encoding='utf8')
    csvWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)

    i = 0
    while True:

        if(countOfTweetsToBeFetched < len(tweets)):
            break # we got all tweets... !!

        #----------------------------------------------------------------#
        # STEP 1: Query Twitter
        # STEP 2: Save the returned tweets
        # STEP 3: Get the next max_id
        #----------------------------------------------------------------#

        # STEP 1: Query Twitter
        if(0 == i):
            # Query twitter for data. 
            results    = api.search(q=querry, count='100', lang='pt')
            
        else:
            # After the first call we should have max_id from result of previous call. Pass it in query.
            results    = api.search(q=querry, include_entities='true', max_id=next_max_id, lang='pt')

        # STEP 2: Save the returned tweets
        for result in results['statuses']:

            tweet_text = preProcessTweetText (result['text'])
            created_at = result["created_at"]
            retweet_count = result["retweet_count"]
            
            if not tweet_text in tweets:
                tweets.append(tweet_text)
                csvWriter.writerow(['|'+str(created_at)+'|', '|'+str(retweet_count)+'|', '|'+tweet_text+'|'])


        # STEP 3: Get the next max_id
        try:
            # Parse the data returned to get max_id to be passed in consequent call.
            next_results_url_params    = results['search_metadata']['next_results']
            next_max_id                = next_results_url_params.split('max_id=')[1].split('&')[0]
        except:
            # No more next pages
            csvFile.close()
            break
        i += 1
