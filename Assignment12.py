'''Ques.1. What is an access token? 
Generate your access token for any API.(for example Twitter,Spotify etc).
Ans.: a.) An access token is an object encapsulating the security identity of a process or 
thread. 
A token is used to make security decisions and to store tamper-proof info.
about some system entity. While a token is generally used to represent only security
information, it is capable of holding additional free-form data that can be attached
while the token is being created.
Tokens can be duplicated without special privilege,
for example: to create a new token with lower levels of access rights to restrict 
the access of a launched application.
An access token is used by Windows when a process or thread tries to interact with
objects that have security descriptors (securable objects). 
An access token is represented by the system object of type Token.'''

'''b.) Access Token	9405746763639807104-t7ZXmVMGnffgsD0QGD9ROwjmCgp60czt
    Access Token Secret	6iwAMMLQhx1VxSoJcviTEydguhdgfgdghwgFRlJUtmRzd0LmiS'''

'''Ques.2. Get the IP address of some common sites like Google, Facebook by using DNS lookup.
Ans2.For Google:
Using nslookup google.com,we get
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4002:803::200e
          172.217.161.14'''

'''For Facebook.com:
Using nslookup facebook.com,we get
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35'''

#Ques.3. Using Tweepy library try to extract tweets from Twitter.
import tweepy
consumer_key='zegJuW3cH1ksGoRshdhjhdgUbcit'
consumer_secret='Gc0GlPJsBeZgSdgfgygGHYHUHghfss6HK5xboqRf1LYkYuWH00mHAtLkHJAAh'
access_token='9405746786359807104-t7ZXmV4dggjxyD0QGD9ROwjmCgp60czt'
access_token_secret='6iwAMMLQhx1VxSoEWcYqvpgsbFRlJUtmRzd0LmiS'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#Internships',lang="en",count=5,tweet_mode="extended")
for tweet in tweets:
	print("")
	print(tweet.full_text)
	print("")

'''Ques.4. What is a difference between library and API . Figure it out with examples.
   Ans.4.: API is a part of library which defines how an application communicates 
   with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities
required for the use case.
For example : Numpy is a library of Python, adding support for large, 
multi-dimensional arrays and matrices, along with a large collection of high-level 
mathematical functions to operate on these arrays.
We can create our own APIs using Python Framework like Django and Flask 
which can be used in websites.
You can follow documentation of Django in order to create your own website with Python.''' 









