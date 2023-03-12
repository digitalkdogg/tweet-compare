import requests
import json
import os
from datetime import datetime
#import datetime
from db_mod import Mysqlconn

tweet_compare_db = Mysqlconn("")

from dotenv import load_dotenv
load_dotenv()

url = "https://twitter154.p.rapidapi.com/user/tweets"

querystring = {"username":"joebiden","limit":"50","user_id":"939091","include_replies":"false"}

headers = {
	"X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
	"X-RapidAPI-Host": os.getenv('X-RapidAPI-Host')
}


print('Getting data from api')
#get from api
response = requests.request("GET", url, headers=headers, params=querystring)
response = json.loads(response.text)

#get from local
#f = open('jbtweets.json')
#response = json.load(f)


for result in response['results']: 
    hasaccount = tweet_compare_db.check_account(result['user']['user_id'])

    if (hasaccount.rowcount==0) :
        print('found an account to insert : '  + result['user']['user_id'])
        thisaccount = {'tweet_account_id': result['user']['user_id'], 'avatar': '', 'tweet_hash': result['user']['user_id'], 'source': 1}
        insert_account = tweet_compare_db.insert_account(thisaccount)
        accountid = insert_account.lastrowid
    else: 
        account = hasaccount.fetchone()
        accountid = account[0]

    hastweet = tweet_compare_db.check_tweet(result['tweet_id'])

    if (hastweet.rowcount==0) :
        print('found a tweet to insert' + result['tweet_id'])
        thistweet = {'tweet_hash': result['tweet_id'], 'content': result['text'].replace("'", r"\'"), 'url': '', 'account_id': accountid ,'tweet_date': datetime.fromtimestamp(result['timestamp'])}
        insert_tweet = tweet_compare_db.insert_tweet(thistweet)
        tweetid = insert_tweet.lastrowid
    else:
        tweet = hastweet.fetchone()
        tweetid = tweet[0]

    hasleft = tweet_compare_db.check_left(tweetid)
    if (hasleft.rowcount==0) :
        print('now inserting into left')
        insert_left = tweet_compare_db.insert_left(tweetid)
        leftid = insert_left.lastrowid
    else:
        left = hasleft.fetchone()
        leftid = left[0]
    print('********************************** \n')
