import tweepy
auth = tweepy.OAuthHandler("h4ZPoeCySEySfD1SKeS5XIewc", "RQKVW7cyT9IUtHjvlI4tG4gAUHoZFCABrZkxl3Sz20LXysBvHo")
auth.set_access_token("709136414286417920-84nEDP8galDkomrxslD6tvJebxZiKUW", "PvlPO3oT1PGa395LQROY6INaFDhLN0Cwo7ySuLwv2aN38")
api = tweepy.API(auth)

tweet = input("What Would You Like To Tweet? ")

latitude =  50.101343
longitude = 8.628527

api.update_status(status =(tweet))
print ("Done!")
