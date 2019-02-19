import tweepy
import twitter_credentials as tc

# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# # TWEET # #

# inputs #

tweet = input("Tweet: ")
reply = input("Reply: ")
user = input("User: ")

# this is so u dont have to put the @<Name> in ur tweet if u wanna reply to someone #

if user == "":
    tweetF = tweet
else:
    tweetF= "@"+(user)+"  "+(tweet)

# some kind of checking if the tweet id is correct #

length = 28 + len(user)
print(length)

replyF = reply[length:]
print(replyF)

# sending the tweet #

api.update_status(status =(tweetF), in_reply_to_status_id =(replyF))
print("-------successfully sent-------")
