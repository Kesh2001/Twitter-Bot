import tweepy
import time

auth = tweepy.OAuthHandler('Vfk4GyALSa0EJWNjJqno10dAO', 'pR0OzfBWNc1FYXjw8g5fBZ6xMKGtuaCrjTJJoxwlY7uas9ocm3')
auth.set_access_token('1292429555752296449-Ct2q3yngfHQ1IGdjpjPBYSPWvPA8CE',
                      'Iz4snP2U8DbKHaTglswoY2i91X13Pqu8JfKmouVKroQG3')

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()  # use if statement to put conditions on people to follow

search_string = 'python'  # write anything
numbersOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numbersOfTweets)):
    try:
        tweet.favorite()  # we can also do here tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
