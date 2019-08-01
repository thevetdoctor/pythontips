# import tweepy
# import sqlite3
import twitter
# from datetime import datetime
from dateutil import parser
# from . import views
# from .views import create
from .models import Tip
# from tweepy import OAuthHandler

consumer_key = "lJ2qmapBCAvUXabumToFA8nny"
consumer_secret = "KpWixWjG5KsQ26OUkzHLuPQCFnbncb2qbVf9FdwLuEQhs2SUYK"
access_token = "1376361980-1YVxPEa7A54QEXO6Yr60bZyAnW7vZakMeQBQPy0"
access_token_secret = "E6BH0eY5x4uJagVR9439ATC02VmRPnUt2OXan2QPzmSCQ"


# Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)
# api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# print(api.VerifyCredentials())


def create(tip_timestamp, tip_text, tip_link, tip_author, tip_published):
    newTip = Tip.objects.create(tip_timestamp=tip_timestamp, tip_text=tip_text,
                                tip_link=tip_link, tip_author=tip_author, tip_published=tip_published)
    # newTip.save()
    # return render(request, showTip, {'tips': tips})
    return newTip

statuses =api.GetUserTimeline(screen_name='animalworldng')
# print([s.text for s in statuses])
for tweet in statuses:
    created_at = parser.parse(tweet.created_at)
    urls = len(tweet.urls)
    # created_at = datetime.strptime(tweet.created_at)
    # print(created_at)
    # print(tweet.created_at, tweet.text, len(tweet.urls), tweet.user.name)
    create(tip_timestamp=created_at, tip_text=tweet.text, tip_link=urls, tip_author=tweet.user.name, tip_published=True)
    # print(status.created_at, status.text, status.user.name)
# print(statuses[0])
print('Done')

# try:
#     api.verify_credentials()
#     tweets = api.user_timeline('python_tip', count=5)
#     for tweet in tweets:
#         create(tweet.created_at, tweet.text, tweet.url, tweet.user.name, tweet.published)
#         print(tweet.created_at, tweet.text, tweet.url, tweet.user.name, tweet.published)
#     print("Authentication OK")
# except:
#     print("Error during authentication")


# # Tweepy class to access Twitter API
# class Streamlistener(tweepy.StreamListener):

# 	def on_connect(self):
# 		print("Connected")

# 	def on_error(self):
# 		if status_code != 200:
# 			print("Error found")
# 			# returning false disconnects the stream
# 			return False

# 	"""
# 	This method reads in tweet data as Json
# 	and extracts the data we want.
# 	"""

# 	def on_data(self, data):

# 		try:
# 			raw_data = json.loads(data)

# 			if 'text' in raw_data:

# 				username = raw_data['user']['screen_name']
# 				created_at = parser.parse(raw_data['created_at'])
# 				tweet = raw_data['text']
# 				retweet_count = raw_data['retweet_count']

# 				if raw_data['place'] is not None:
# 					place = raw_data['place']['country']
# 					print(place)
# 				else:
# 					place = None

# 				location = raw_data['user']['location']

# 				#insert data just collected into MySQL database
# 				# connect(username, created_at, tweet, retweet_count, place, location)
# 				# print("Tweet colleted at: {} ".format(str(created_at)))
# 		except Error as e:
# 			print(e)


# if __name__ == '__main__':
# 	while True:
# 	    print("Initialising Connection...")
# 	    time.sleep(2)

# 	# create instance of Streamlistener
# # listener = Streamlistener(api)
# # stream = tweepy.Stream(auth, listener)

# # track = ['python_tips']
# # # choose what we want to filter by
# # stream.filter(track=track, languages=['en'])
# # import tweepy
# # # from tweepy import OAuthHandler, API

# # import sqlite3


# # # Authenticate to Twitter
# # auth = tweepy.OAuthHandler("lJ2qmapBCAvUXabumToFA8nny",
# #                            "KpWixWjG5KsQ26OUkzHLuPQCFnbncb2qbVf9FdwLuEQhs2SUYK")
# # auth.set_access_token("1376361980-1YVxPEa7A54QEXO6Yr60bZyAnW7vZakMeQBQPy0",
# #                       "E6BH0eY5x4uJagVR9439ATC02VmRPnUt2OXan2QPzmSCQ")

# # api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# # try:
# #     api.verify_credentials()
# #     tweets = api.user_timeline('python_tip')
# #     for tweet in tweets:
# #         print(tweet)
# #     print("Authentication OK")
# # except:
# #     print("Error during authentication")
