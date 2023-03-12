import pymysql
import os

pymysql.install_as_MySQLdb()

class Mysqlconn:
    def __init__(self, connect): 

        from dotenv import load_dotenv
        load_dotenv()
       
        self.connect = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USERNAME'), 
        password = os.getenv('PASSWORD'),
        db=os.getenv('DB'),
        )

    def check_account(self, id): 
        
        cur = self.connect.cursor()
        query = f"SELECT * FROM account where tweet_account_id = '{id}'"

        cur.execute(query)
        #results = cur.fetchall()
        return cur

    def check_tweet(self, tweet_hash): 
        
        cur = self.connect.cursor()
        query = f"SELECT * FROM tweet_details where tweet_hash = '{tweet_hash}'"

        cur.execute(query)
        return cur

    def check_left(self, tweet_id): 
        
        cur = self.connect.cursor()
        query = f"SELECT * FROM `left` where tweetid = {tweet_id}"
        cur.execute(query)
        return cur

    def check_right(self, tweet_id): 
        
        cur = self.connect.cursor()
        query = f"SELECT * FROM `right` where tweetid = {tweet_id}"
        cur.execute(query)
        return cur


    def insert_account(self, account) :
        query = f"INSERT INTO account (tweet_account_id, avatar, tweet_hash, source) VALUES ('{account['tweet_account_id']}', '{account['avatar']}', '{account['tweet_hash']}', '{account['source']}')"
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        return cur

    def insert_tweet(self, tweet) :
        query = f"INSERT INTO tweet_details (tweet_hash, content, url, account_id, tweet_date) VALUES ('{tweet['tweet_hash']}', '{tweet['content']}', '{tweet['url']}', '{tweet['account_id']}', '{tweet['tweet_date']}')"
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        return cur
    
    def insert_left(self, tweetid) :
        query = f"INSERT INTO `left` (tweetid) VALUES ('{tweetid}')"
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        return cur

    def insert_right(self, tweetid) :
        query = f"INSERT INTO `right` (tweetid) VALUES ('{tweetid}')"
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        return cur