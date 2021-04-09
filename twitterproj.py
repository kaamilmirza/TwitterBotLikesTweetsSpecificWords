import tweepy #please use pip install to get this library if you don't have or if you don't know how, search how to install external python libs
import time
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #get consumer key, consumer secret, access token, and access token secret from twitter, google about it or watch some youtubue video
auth.set_access_token(access_token, access_token_secret) #developers account/option enabled for twitter is must to get tokens it takes about 10 minutes to do it

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = '' #enter the string that you want to make the search for
numberofTweets = 30

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberofTweets)): #has limiter to make sure twitter doesn't think we spamming
	try:
		tweet.favorite()
		print('I liked that tweet') #just to print everything is going fine 
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break




