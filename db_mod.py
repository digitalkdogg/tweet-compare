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

    def check_account(self): 
        print(self.connect)
        cur = self.connect.cursor()
        query = f"SELECT * FROM account where tweet_account_id = '107780257626128497'"

        cur.execute(query)
        results = cur.fetchall()
        return results