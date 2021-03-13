import tweepy
import json


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        y = json.loads(data)
        print((y['user']['screen_name']))
        print(y['text'])
        return True

    def on_error(self, status):
        print(status)
