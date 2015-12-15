__author__ = 'vincentpham'
import psycopg2, psycopg2.extras

# this is the set of functions I used to build my database
# the source of my data is from reddit that was collected in September
# To find out more about the collection method visit: 
#       https://github.com/reddit-analyzer/data_acq
#   In short, it contains data collected from 5 subreddits and the front page of
#   Reddit for a one week period. Data are collected from the 20 first threads
#   along with comments made by user at the time of collection.
#
# here are also functions for dropping and creating the db


DB_DSN = "host=db.cvu5a6kuxniq.us-west-2.rds.amazonaws.com dbname=db_restaurants user=dbuser password=dbpassword"

# path of the input data file
THREADS_PATH = r"/Users/vincentpham/Desktop/all_thread.csv"
COMMENTS_PATH = r"/Users/vincentpham/Desktop/all_comments.csv"


def drop_table():
    """
    drops the table 'threads' and  'comments' if it exists
    :return:
    """
    try:
        query1 = "drop table if exists threads;"
        query2 = "drop table if exists comments;"
        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor()
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
    except psycopg2.Error as e:
       print e.message
    else:
       cur.close()
       conn.close()

    return

def createThreadsTable():
    """
    creates a postgres table 'threads'
    :return:
    """
    try:
        query = '''CREATE TABLE threads
                    (fp TEXT
                    ,subreddit_name TEXT
                    ,reddit_username TEXT
                    ,post_title TEXT
                    ,post_text TEXT
                    ,thread_id TEXT
                    ,num_posts INT
                    ,domain_name TEXT
                    ,gilded_score INT
                    ,post_score INT
                    ,ranking INT
                    ,post_time TIMESTAMP
                    ,now_time TIMESTAMP
                    ,post_url TEXT
                    );'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except psycopg2.Error as e:
       print e.message
    else:
       cur.close()
       conn.close()
    return

def createCommentsTable():
    """
    creates a postgres table 'comments'
    :return:
    """
    try:
        query = '''CREATE TABLE comments
                    (fp TEXT
                    ,thread_id TEXT
                    ,comment_id TEXT
                    ,comment_usr TEXT
                    ,usr_id TEXT
                    ,comment_upvotes INT
                    ,cleaned_comment TEXT
                    ,comment_position INT
                    ,length_comment INT
                    ,num_replies INT
                    ,edited BOOLEAN
                    ,comment_gilds INT
                    ,comment_created TIMESTAMP
                    ,now_time TIMESTAMP
                    );'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except psycopg2.Error as e:
       print e.message
    else:
       cur.close()
       conn.close()
    return

def create_table():
    '''
    Calls all functions that creates a table
    :return:
    '''
    createThreadsTable()
    createCommentsTable()

    return

def insert_data():
    """
    inserts the data using copy_expert into 'threads' and 'comments' table
    :return:
    """
    try:

        query_threads = '''COPY threads FROM stdin DELIMITER ',' CSV;'''
        query_comments = '''COPY comments FROM stdin DELIMITER ',' CSV;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor()


        with open(THREADS_PATH, 'r') as f:
            cur.copy_expert(sql = query_threads, file = f)
        print "table threads created"

        with open(COMMENTS_PATH, 'r') as f:
            cur.copy_expert(sql = query_comments, file = f)
        print "table comments created"

        conn.commit()
    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()
    return

if __name__ == '__main__':
    # running this program as a main file will perform ALL the ETL
    # it will extract and copy the data from the file to the database

    # drop the db
    print "dropping table"
    drop_table()

    # create the db
    print "creating table"
    create_table()

    # insert the data
    print "inserting data"
    insert_data()
