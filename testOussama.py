import tweepy
import redis
import  nltk
from  nltk.corpus  import  treebank

# The user credential variables to access Twitter API
access_token = "243510610-uW7TEaqISBwB86VCfQh0gczU6WaTwIX4xr2CHvt3"
access_token_secret = "lGmSgFPFzAPFLQ2THFqEG7OUg8akd5WusbijZuh9UlqHl"
consumer_key = "QtM1L0ppK6KPC2OXaAqRHwsrP"
consumer_secret = "1AYVWMuePpHWRGgR2AIiuM9fGp0bAVoGF4mmPUiqXoIpnDRHwh"

# Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# phrase = "" "salut Oussama cv """
#
#
# jetons  =  nltk . word_tokenize ( phrase )
# print(jetons)
#
# tagged=[('At', 'IN'), ('huit', 'CD'), ("heures", 'JJ'), ('on', 'IN'),
# ('Jeudi', 'NNP '), (' matin ',' NN ')]
# entities  =  nltk . morceau . ne_chunk ( tagged )
# t  =  treebank . parsed_sents ( entities) [ 0 ]
# t.draw()


query = 'Libya'
max_tweets = 100

public_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

# Results
#assembler les tweet
tweetString=[]
i=0
for tweet in public_tweets:
   tweetString.append(tweet.text)
   i=i+1
   print( str(i)+" "+tweet.text)


r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('tweet', tweetString)

B=r.get('tweet')
for x in B :
   print(x.text)

