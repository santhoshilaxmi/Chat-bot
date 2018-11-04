# starting to create chat bot on 4-11-2018
import numpy
import random
import sqlite3
import json
from datetime import datetime

timeframe = '2005-12'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c= connection.cursor()

    
def format_data(data):
    data = data.replace("\n"," newlinechar ").replace("\r"," newlinechar ").replace('"',"'")
    return data
   
#def create_table():
#    c.execute("""CREATE TABLE IF NOT EXISTS 
#              parent_reply(parent_id TEXT PRIMARY KEY,
#              comment_id TEXT UNOQUE,
#              parent TEXT,
#              Comment TEXT,
#              subreddit TEXT,
#              score INT,
#              unix INT)""")
    
def delete_table():
    c.execute("""DROP TABLE IF EXISTS parent_reply""")
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS 
              parent_reply(parent_id TEXT,
              body TEXT,
              subreddit TEXT,
              score INT,
              created_utc INT,
              row_counter INT PRIMARY KEY)""")
    print("table created")
    c.execute('PRAGMA table_info(parent_reply)')
    print c.fetchall()
    
def sql_insert_func(parent_id,body,subreddit,score,created_utc,row_counter):
    try:
        #print(parent_id+"***"+body+"***"+subreddit+"***"+score+"***"+created_utc+"***"+row_counter)
        sql="""INSERT INTO parent_reply values ('parent_id','body','subreddit','score','created_utc','row_counter')"""
        print("***************")
        #transaction_bldr(sql)
        c.execute(sql)
        #print("calling transaction _bldr")
        connection.commit()
    except Exception as e:
        print('inserted not successfull',e)
        
def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)
    print("appended")
    if len(sql_transaction)>10:
        print("started execution")
        c.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                c.execute(s)
                print("executed")
            except:
                pass
        connection.commit()
        sql_transaction=[]
                
    
if __name__=="__main__":
#      delete_table()
 
 
#        create_table()
        row_counter=0
        paired_rows=0
         
#     #   with open("D:/Chat Bot/reddit one month data/RC_{}".format(timeframe+"-2"),buffering=5) as f:
#        with open("D:/Chat Bot/reddit one month data/RC_2005-12-2.txt",buffering=5) as f:
#             for row in f:
#                # print(row)
        row_counter=row_counter+1
        print(row_counter)
#                 row = json.loads(row)
#                 parent_id=row['parent_id']
#                 #id1=row['id']
#                 body=format_data(row['body'])
#                 created_utc=row['created_utc']
#                 subreddit=row['subreddit']
#                 score=row['score']
#                 #parent_data=find_parent(parent_id)
        print(type("17878"))
        print(type("I don\u00e2\u0080\u0099t know w Client has taken cool concept that\u00e2\u0080\u0099s just beginning to bnd pasting phrases."))
        print(type("reddit.com"))
        print(type(1))
        print(type(1134))
        print(type(1))          
        sql_insert_func("17878","I don\u00e2\u0080\u0099t know where they came up with this stuff, but Qube Web Search Client has taken the market by surprise. This is a cool concept that\u00e2\u0080\u0099s just beginning to blossom. You can save time by copying and pasting words and phrases.","reddit.com",1,1134,1)
#       
# 


            
            
            
        
    
    




