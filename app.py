from flask import Flask
import tweepy
import streaming

app = Flask(__name__)

consumer_key = "UwNbJ8l6E6VrEi32y70yqun0Y"
consumer_secret = "qt30g5cgZSls7hpcssYzym1GCmoGamliyUfUFQCroK8jh2nGYa"
access_token = "1370678523468390401-TCDxmbNz1CjJsCIVNpMj4PIaBSRwQ5"
access_token_secret = "g3kbIoJFvo6zDErOKMjzJWOXHit6BsXgKSyFZY8Lqf2bd"

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
