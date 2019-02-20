import tweepy
import twitter_credentials as tc

# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# # TWEET # #

cred = (" www.github.com/scurex")


loop = True
while loop:

# inputs #
 print('www.github.com/scurex')
 
 tweet = input("Tweet: ")
 reply = input("Reply: ")
 user = input("User: ")

# this is so u dont have to put the @<Name> in ur tweet if u wanna reply to someone #

 if user == "":
    tweetF = tweet
 else:
    tweetF= "@"+(user)+"  "+(tweet)

# some kind of error checking #

 length = 28 + len(user)
 print(length)

 replyF = reply[length:]
 print(replyF)


# checks if tweet is too long and if yes how much characters u have to delete

 if len(tweetF) + len(cred) > 280:
    errLong = (len(tweetF) + len(cred)) - 280
    
    tweet = tweet[:errLong]
    tweetF = ""
    reply = ""
    user = ""
    
    print("---error! your tweet is " + str(errLong) + " characters too long---")
    print("--- TRY AGAIN ---")
    
    continue
    
 else:
# sending the tweet #
    api.update_status(status =(tweetF+(cred)), in_reply_to_status_id =(replyF))


    print("-------successfully sent-------")
    
    retry = input("Send another Tweet? (y/n) ")
    
    if retry == ("y"):
        continue
    elif retry == ("n"):
        print("okay byee")
        break
    else:
        print(retry + (" is not an available option"))
        break
 
    
    
