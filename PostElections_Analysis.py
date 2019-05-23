import csv
import tweepy
from textblob import TextBlob

bjp_p=0
bjp_n=0
bjp_b=0
cong_p=0
cong_b=0
cong_n=0

consumer_key = 'DVVX885fe4Uw4aMlnyttFpjaY'
consumer_skey = 'aOhBlVgiSGirlTQaWOZguO5mvyGUgMqeuUR9P91OVvtf2jowWQ'
access_token = '147164311-rTzFPU9nzFR81GR1KW3tuNwnbOpge9dYYWfN79Rc'
access_token_sk = '95T1ZupqsQyjvbsvB8QLijSaQzhOOB2SwVHClDXxMFq1q'

auth = tweepy.OAuthHandler(consumer_key, consumer_skey)
auth.set_access_token(access_token, access_token_sk)

api = tweepy.API(auth, wait_on_rate_limit=True)


bjp_tweets = tweepy.Cursor(api.search, q='bjp', count=3000, lang="en", since="2019-05-23").items()
cong_tweets = tweepy.Cursor(api.search, q='congress', count=3000, lang="en", since="2019-05-23").items()

print("BJP")
for tweet in bjp_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print ('Positive')
        bjp_p+=1
    elif analysis.sentiment[0]==0:
        print('Neutral')
        bjp_b+=1
    else:
        print ('Negative')
        bjp_n+=1
print("")

print("CONGRESS")
for tweet in cong_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print ('Positive')
        cong_p+=1
    elif analysis.sentiment[0]==0:
        print('Neutral')
        cong_b+=1
    else:
        print ('Negative')
        cong_n+=1
print("")

print("BJP POSITIVE TWEETS:",bjp_p)
print("BJP NEUTRAL TWEETS:",bjp_b)
print("BJP NEGATIVE TWEETS:",bjp_n)

print("CONG POSITIVE TWEETS:",cong_p)
print("CONG NEUTRAL TWEETS:",cong_b)
print("CONG NEGATIVE TWEETS:",cong_n)
