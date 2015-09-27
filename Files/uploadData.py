import database

def uploadData(full_thread_csvfilename, full_comments_csvfilename, database_name, password_string, schema_name,
               thread_tablename, comments_tablename, user_name, hostname):

    mydatabase = myDatabase(full_thread_csvfilename, full_comments_csvfilename, database_name, password_string,
                      schema_name, thread_tablename, comments_tablename, user_name,
                      hostname)


    mydatabase.createDatabase()
    mydatabase.createSchema()
    mydatabase.createThreadTable()
    mydatabase.createCommentsTable()
    mydatabase.copyTable()
    return "Database up!"
