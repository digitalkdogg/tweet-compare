import requests
import json
from db_mod import Mysqlconn

tweet_compare_db = Mysqlconn("")

def convertdate(datestr):
    datearr = datestr.split('T')
    mdy = datearr[0]
    hms = datearr[1].split('.')
    return mdy + ' ' + hms[0]

print('getting data from api')

url = "https://truthsocial.com/api/v1/accounts/107780257626128497/statuses?exclude_replies=true&with_muted=false"

response = requests.request("GET", url)
jsonres = json.loads(response.text)

for truths in jsonres:
    hasaccount = tweet_compare_db.check_account(truths['account']['id'])
    if (hasaccount.rowcount==0) :
        print('found an account to insert ' + truths['account']['id'])
        thisaccount = {'tweet_account_id': truths['account']['id'], 'avatar': truths['account']['avatar'], 'tweet_hash': truths['account']['id'], 'source': 2}
        insert_account = tweet_compare_db.insert_account(thisaccount)
        accountid = insert_account.lastrowid
    else: 
        account = hasaccount.fetchone()
        accountid = account[0]

    hastweet = tweet_compare_db.check_tweet( truths['id'])
    if (hastweet.rowcount==0) :
        print('found a tweet to insert ' + truths['id'])
        thistweet = {'tweet_hash':  truths['id'], 'content': truths['content'].replace("'", r"\'"), 'url': truths['url'], 'account_id': accountid, 'tweet_date': convertdate(truths['created_at'])}
        insert_tweet = tweet_compare_db.insert_tweet(thistweet)
        tweetid = insert_tweet.lastrowid
    else:
        tweet = hastweet.fetchone()
        tweetid = tweet[0]

    hasright = tweet_compare_db.check_right(tweetid)
    if (hasright.rowcount==0) :
        print('now I am inserting to the right')
        insert_right = tweet_compare_db.insert_right(tweetid)
        rightid = insert_right.lastrowid
    else:
        right = hasright.fetchone()
        rightid = right[0]

    print('********************************\n')