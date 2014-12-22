# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import re

def pre_process_tweet_text(tweet_text):
    """Removes uninformative words and characters from the text of a tweet.
    
     Parameters
     ----------
     tweet_text : string
        the text extracted from a given tweet.

     Returns
     -------
     tweet_text : string
        the pre-processed tweet text.
    """

    #Convert to lower case
    tweet_text = tweet_text.lower()

    #Convert www.* or https?://* to URL
    tweet_text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweet_text)

    #Convert @username to AT_USER
    tweet_text = re.sub('@[^\s]+','AT_USER', tweet_text)    

    #Remove additional white spaces
    tweet_text = re.sub('[\s]+', ' ', tweet_text)

    #Replace #word with word
    tweet_text = re.sub(r'#([^\s]+)', r'\1', tweet_text)
    
    #trim
    tweet_text = tweet_text.strip('\'"')

    # removing other uninformative characters
    tweet_text = tweet_text.replace('\n', '')
    tweet_text = tweet_text.replace('\'', '')
    tweet_text = tweet_text.replace('\"', '')
    tweet_text = tweet_text.replace(';', '')
    tweet_text = tweet_text.replace('|', '')
    tweet_text = tweet_text.replace(':', '')
    tweet_text = tweet_text.replace('.', '')
    tweet_text = tweet_text.replace('?', '')
    tweet_text = tweet_text.replace('!', '')
    tweet_text = tweet_text.replace('\\', '')
    tweet_text = tweet_text.replace(',', '')
    tweet_text = tweet_text.replace('/', '')

    #look for 2 or more repetitions of character
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
    tweet_text = pattern.sub(r"\1\1", tweet_text)
    
    return tweet_text
#end