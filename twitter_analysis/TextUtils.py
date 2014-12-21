import re

def preProcessTweetText(tweetText):

    #Convert to lower case
    tweetText = tweetText.lower()

    #Convert www.* or https?://* to URL
    tweetText = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweetText)

    #Convert @username to AT_USER
    tweetText = re.sub('@[^\s]+','AT_USER', tweetText)    

    #Remove additional white spaces
    tweetText = re.sub('[\s]+', ' ', tweetText)

    #Replace #word with word
    tweetText = re.sub(r'#([^\s]+)', r'\1', tweetText)
    
    #trim
    tweetText = tweetText.strip('\'"')

    # removing other uninformative characters
    tweetText = tweetText.replace('\n', '')
    tweetText = tweetText.replace('\'', '')
    tweetText = tweetText.replace('\"', '')
    tweetText = tweetText.replace(';', '')
    tweetText = tweetText.replace('|', '')
    tweetText = tweetText.replace(':', '')
    tweetText = tweetText.replace('.', '')
    tweetText = tweetText.replace('?', '')
    tweetText = tweetText.replace('!', '')
    tweetText = tweetText.replace('\\', '')
    tweetText = tweetText.replace(',', '')
    tweetText = tweetText.replace('/', '')

    #look for 2 or more repetitions of character
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
    tweetText = pattern.sub(r"\1\1", tweetText)
    
    return tweetText
#end