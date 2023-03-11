import requests
import json
import os
import pymysql
from datetime import datetime

pymysql.install_as_MySQLdb()

class mysqlconn:
    def connect():
        from dotenv import load_dotenv
        load_dotenv()
       
        conn = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USERNAME'), 
        password = os.getenv('PASSWORD'),
        db=os.getenv('DB'),
        )
        return conn

    def inserttweet(data): 
        cur= connection.cursor()
        query = f"SELECT * FROM tweets where tweet_id = '{data['tweet_id']}'"
        cur.execute(query)
            
        if cur.rowcount == 0:
            #print('i')
            query = f"INSERT INTO tweets (tweet_id, ts_content, source, created_at, url, accountid) VALUES ('{data['tweet_id']}', '{data['ts_content']}', '{data['source']}', '{data['created_at']}', '{data['url']}', '{data['accountid']}')"
            cur.execute(query)
            connection.commit()

    def insertaccount(account): 
        cur= connection.cursor()
        query = f"SELECT * FROM account where id = '{account['id']}'"
        cur.execute(query)
            
        if cur.rowcount == 0:
            #print('i')
            query = f"INSERT INTO account (id, avatar) VALUES ('{account['id']}', '{account['avatar']}')"
            cur.execute(query)
            connection.commit()

def convertdate(datestr):
    datearr = datestr.split('T')
    mdy = datearr[0]
    hms = datearr[1].split('.')
    return mdy + ' ' + hms[0]

      
if __name__ == "__main__" :
    #connection = mysqlconnect()
    connection = mysqlconn.connect()

url = "https://truthsocial.com/api/v1/accounts/107780257626128497/statuses?exclude_replies=true&with_muted=false"


response = requests.request("GET", url)
jsonres = json.loads(response.text)

searchterm = ' woke'

for truths in jsonres:
    if type(truths['quote']) is dict:
        content = truths['quote']['content'].lower()
        
        if (content.find(searchterm.lower())>=0):

            account = {
                'id': truths['account']['id'],
                'avatar': truths['account']['avatar']
            }
            mysqlconn.insertaccount(account)

            data = {
                'tweet_id': truths['id'], 
                'ts_content': truths['quote']['content'].replace("'", r"\'"),
                'source': 'ts',
                'created_at': convertdate(truths['created_at']),
                'url': truths['url'],
                'accountid': truths['account']['id']
                }
            mysqlconn.inserttweet(data)

connection.close()