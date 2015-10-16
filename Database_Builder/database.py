#Logistics
#Throw error if praw library not installed.
import os

try:
    import psycopg2
except ImportError:
    print "psycopg2 library not found."

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class myDatabase:
    def __init__(self,thread_csv_filename, comments_csv_filename, database_name, password_string,
                 schema_name, thread_tablename, comments_tablename, user_name, host_name):
        self.thread_csv_filename = thread_csv_filename
        self.comments_csv_filename = comments_csv_filename
        self.database_name = database_name
        self.password_string = password_string
        self.schema_name = schema_name
        self.thread_tablename = thread_tablename
        self.comments_tablename = comments_tablename
        self.user_name = user_name
        self.host_name = host_name

    def changeDir(self, dir_of_files):
        try:
            os.chdir(dir_of_files)
        except:
            return "No such directory"
        return

    def createDatabase(self):
        #create connection to highest level database and create a database
        conn = psycopg2.connect('user = %s host = %s password = %s' % (self.user_name, self.host_name, self.password_string))
        cur = conn.cursor()
        cur.execute('SELECT datname FROM pg_catalog.pg_database;')
        existing_db = cur.fetchall()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        if self.database_name[0].isupper() == True:
            new_db_name = self.database_name[:1].lower() + self.database_name[1:]
        else:
            new_db_name = self.database_name
        try:
            cur.execute('CREATE DATABASE %s' % new_db_name)
            return "%s created!" % new_db_name
        except:
            print "Database already exists!"
        finally:
            conn.close()

    def accessDatabase(self):
        #access database
        #make sure first letter of database name is lowercase by convention
        if self.database_name[0].isupper() == True:
            new_db_name = self.database_name[:1].lower() + self.database_name[1:]
        else:
            new_db_name = self.database_name
        conn = psycopg2.connect('dbname = %s user = %s host = %s password = %s'
							% (new_db_name, self.user_name, self.host_name, self.password_string))
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
                    ,edited BOOLEAN
                    ,comment_gilds INT
                    ,comment_created TIMESTAMP
                    ,now_time TIMESTAMP);''')
        cur.execute('commit;')
        conn.close()
        return "Comments table created"

    def copyTable(self):
        conn, cur = self.accessDatabase()
        #copy csv file to table
        thread_path = str(os.path.join(os.getcwd(), self.thread_csv_filename))
        comments_path = str(os.path.join(os.getcwd(), self.comments_csv_filename))
        try:
            cur.execute('''COPY %s
                        FROM '%s'
                        DELIMITER ',' CSV;''' % (self.schema_name + "." + self.thread_tablename, thread_path))
            cur.execute('''COPY %s
                        FROM '%s'
                        DELIMITER ',' CSV;''' % (self.schema_name + "." + self.comments_tablename, comments_path))
        except:
            return "No such file or directory"
        cur.execute('commit;')
        conn.close()
        return "Data copied"

    def dropTable(self, tablename):
        conn, cur = self.accessDatabase()
        #drop table
        cur.execute('''DROP TABLE %s;''' % tablename)
        cur.execute('commit;')
        conn.close()
        return "Table dropped"