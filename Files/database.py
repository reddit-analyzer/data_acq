#Logistics
#Throw error if praw library not installed.
try:
    import psycopg2
except ImportError:
    print "psycopg2 library not found."

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class database:
    def __init__(self,thread_csv_filename, comments_csv_filename, database_name, table_name, password_string,
                 schema_name, thread_tablename, comments_tablename, user_name, host_name):
        self.thread_csv_filename = thread_csv_filename
        self.comments_csv_filename = comments_csv_filename
        self.database_name = database_name
        self.table_name = table_name
        self.password_string = password_string
        self.schema_name = schema_name
        self.thread_tablename = thread_tablename
        self.comments_tablename = comments_tablename
        self.user_name = user_name
        self.host_name = host_name

    def createDatabase(self):
        #create connection to highest level database and create a database
        conn = psycopg2.connect('user = %s host = %s password = %s' % (self.user_name, self.host_name, self.password_string))
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute('''create database %s''' % self.database_name)
        conn.close()
        return "%s created!" % self.database_name

    def accessDatabase(self):
        #access database
        conn = psycopg2.connect('dbname = %s user = %s host = %s password = %s'
							% (self.database_name, self.user_name, self.host_name, self.password_string))
        cur = conn.cursor()
        return conn, cur

    def createSchema(self):
        conn, cur = self.accessDatabase()
        cur.execute('CREATE SCHEMA %s;' % self.schema_name)
        cur.execute('commit;')
        conn.close()
        return "Schema created"

    def createThreadTable(self):
        conn, cur = self.accessDatabase()
        cur.execute('''CREATE TABLE '''+ self.schema_name + '.' + self.thread_tablename +'''
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
        conn.close()
        return "Thread table created"

    def createCommentsTable(self):
        conn, cur = self.accessDatabase()
        cur.execute('''CREATE TABLE '''+self.schema_name + '.' + self.comments_tablename +'''
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
                    ,edited INT
                    ,comment_gilds INT
                    ,comment_created TIMESTAMP
                    ,now_time TIMESTAMP);''')
        cur.execute('commit;')
        conn.close()
        return "Comments table created"

    def copyTable(self):
        conn, cur = self.accessDatabase()
        #copy csv file to table
        cur.execute('''COPY %s
                    FROM '%s'
                    DELIMITER ',' CSV;''' % (self.schema_name + "." + self.thread_tablename, self.thread_csv_filename))

        cur.execute('''COPY %s
                    FROM %s
                    DELIMITER ',' CSV;''' % (self.schema_name + "." + self.comments_tablename, self.comments_csv_filename))
        conn.close()
        return "Data copied"