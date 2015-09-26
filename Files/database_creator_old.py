#Logistics
#Throw error if praw library not installed.
try:
    import psycopg2
except ImportError:
    print "psycopg2 library not found."

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def databaseCreator(csv_filename, database_name, table_name, password_string, user_name = 'postgres', host_name = 'localhost', schema_name = 'TOP25'):
    #create connection to highest level database and create a database
    conn = psycopg2.connect('user = %s host = %s password = %s' % (user_name, host_name, password_string))
    cur = conn.cursor()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute('''create database %s''' % database_name)
    conn.close()

    #connect to newly created database
    conn = psycopg2.connect('dbname = %s user = %s host = %s password = %s'
							% (database_name, user_name, host_name, password_string))
    cur = conn.cursor()

    #create SCHEMA
    cur.execute('CREATE SCHEMA %s;' % schema_name)
    cur.execute('commit;')

    #create table called MYFRIENDS
    cur.execute('''CREATE TABLE '''+ schema_name + '.' + table_name +'''
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
                    ,post_url TEXT);''')
    cur.execute('commit;')

    #copy csv file to table
    cur.execute('''COPY %s
                   FROM '%s'
                   DELIMITER ',' CSV;''' % (schema_name + "." + table_name, csv_filename))

    cur.execute('commit;')
    conn.close()
    return "Database created"