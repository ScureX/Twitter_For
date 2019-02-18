import tweepy
import twitter_credentials as tc

# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# # TWEET # #

tweet = input("Tweet: ")
reply = input("Reply to: ")

api.update_status(status =(tweet), in_reply_to_status_id =(reply))
print ("-------successfully sent-------")
