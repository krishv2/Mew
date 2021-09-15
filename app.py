from flask import Flask
import tweepy
import streaming

app = Flask(__name__)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
myStreamListener = streaming.MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)


@app.route("/")
def home():
    myStream.filter(track=['python'], is_async=True)
    return 'working...'


if __name__ == '__main__':
    print('hello')
