import tweepy, time, sys

import sys

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
from twitter_credentials import *
from db_config import *

class PrintBot(StreamListener):

	def on_data( self, data):
		print(json.loads(data)["text"])
		return True

	def on_error(self, status):
		print(status)

class MongoBot(StreamListener):
	def __init__(self, collection):
		self.collection = collection

	def on_data( self, data):
		json_data = json.loads(data)
		db[self.collection].insert_one(json_data)

	def on_error(self, status):
		print(status)

def setup_streams():
	for topic in ["nba", "trump"]:
		l = PrintBot(topic)
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)

		stream.filter(track = [ 'nba' ])

if __name__ == "__main__":
	#l = PrintBot('nba')
	setup_streams()

	#auth = OAuthHandler(consumer_key, consumer_secret)
	#auth.set_access_token(access_token, access_token_secret)
	#stream = Stream(auth, l)

	#stream.filter(track = [ 'nba' ])