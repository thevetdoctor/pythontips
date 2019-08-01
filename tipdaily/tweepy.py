import tweepy
import sqlite3

# print tweepy
# from tweepy import OAuthHandler, API

# Authenticate to Twitter
auth = tweepy.auth.OAuthHandler("lJ2qmapBCAvUXabumToFA8nny",
                           "KpWixWjG5KsQ26OUkzHLuPQCFnbncb2qbVf9FdwLuEQhs2SUYK")
auth.set_access_token("1376361980-1YVxPEa7A54QEXO6Yr60bZyAnW7vZakMeQBQPy0",
                      "E6BH0eY5x4uJagVR9439ATC02VmRPnUt2OXan2QPzmSCQ")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    tweets = api.user_timeline('python_tip')
    for tweet in tweets:
        print(tweet.user.name, tweet.text, tweet.description)
    print("Authentication OK")
except:
    print("Error during authentication")


# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):

	def on_connect(self):
		print("Connected")

	def on_error(self):
		if status_code != 200:
			print("Error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""

	def on_data(self, data):

		try:
			raw_data = json.loads(data)

			if 'text' in raw_data:

				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				connect(username, created_at, tweet, retweet_count, place, location)
				print("Tweet colleted at: {} ".format(str(created_at)))
		except Error as e:
			print(e)


if __name__ == '__main__':
	while True:
	    print("Initialising Connection...")
	    time.sleep(2)

	# create instance of Streamlistener
# listener = Streamlistener(api)
# stream = tweepy.Stream(auth, listener)

# track = ['python_tips']
# # choose what we want to filter by
# stream.filter(track=track, languages=['en'])
