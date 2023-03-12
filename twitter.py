import requests
import json
import os
from db_mod import Mysqlconn

tweet_compare_db = Mysqlconn("")

account = tweet_compare_db.check_account()
print(account)

from dotenv import load_dotenv
load_dotenv()

url = "https://twitter154.p.rapidapi.com/user/tweets"

querystring = {"username":"joebiden","limit":"2","user_id":"939091","include_replies":"false"}

headers = {
	"X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
	"X-RapidAPI-Host": os.getenv('X-RapidAPI-Host')
}

#get from api
#response = requests.request("GET", url, headers=headers, params=querystring)
#response = json.loads(response.text)

#get from local
f = open('jbtweets.json')
response = json.load(f)

for result in response['results']: 
    print("**************new line **************************\n")
    print(result)

