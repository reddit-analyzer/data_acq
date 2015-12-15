reddit-analyzer 
===============
Our mission is to scrape data from [Reddit](https://www.reddit.com/) and analyze the data.
We use the [praw library](https://praw.readthedocs.org/en/stable/) in python in order to access the API. 


### Collecting The Data (Data_Collection):

Currently we are focused on obtaining the top 25 threads from the front page and 5 other subreddits. 
We are also collecting data on ~ 40 top level comments from the top 25 threads,
and information about the users who either posted the top threads or comments. 

##### Subreddits of interest:
* [Front Page (fp)](https://www.reddit.com/)
* [worldnews](https://www.reddit.com/r/worldnews/)
* [aww](https://www.reddit.com/r/aww/)
* [nottheonion](https://www.reddit.com/r/nottheonion/)
* [television](https://www.reddit.com/r/television/)
* [AnimalsBeingJerks](https://www.reddit.com/r/AnimalsBeingJerks/)

#### Files:

######thread_getter.py
    threadData(list_items, now_time, subreddit_name)
    
######comment_getter.py
    commentData(comments_list, now_time, subreddit_name)
    
######user_getter.py
    userData(list_items, subreddit_name)
    
######subreddit_getter.py
    subredditData(subreddits_data = "all", save_dir = None, limit = 0)
      subreddits_data: 1 for first chunk
                       2 for second chunk
                       "all" for first and second chunk
                       custom list of subreddits
                       
      save_dir: path of directory to save csv,
                None = working directory
      
      limit: number of thread to capture
             limit = 0 for first page 
  
    submissionData(subreddit_name, limit = 0)
      Get data for one subreddit

######csv_getter.py
    csvSave(list_of_list, outfile)

### Importing Collected Data (Database_Builder):

#### Files:
######csv_adder.py
    csvGlue(dir_csv_files)
    csv_writer(csv_list, outfile_name)

######database.py
    changeDir(self, dir_of_files)
    createDatabase(self)
    accessDatabase(self)
    createSchema(self)
    createThreadTable(self)
    createCommentsTable(self)
    copyTable(self)
    dropTable(self, tablename)
    
######uploadData.py
     uploadData(full_thread_csvfilename, full_comments_csvfilename, database_name, password_string, schema_name,
                thread_tablename, comments_tablename, user_name, hostname)
                
### Analyzing The Data (Analysis):

#### Python:
######analysis.py 
     plot_common_phrases(password)
     '''scatterplot of the most commonly occuring phrases and the average upvote'''
     
######domaningraph.py
     '''generates subredditPlot.pdf'''

######graphcomments.py

######graphtest.py

#### R:
######commentwordcloud.R

######length_upvotes.R

#### SQL:
######exploration1.sql

#### csv_output:
contains outputs queried from SQL for reading into R and/or Python

#### output:
contains graph outputs from R and/or Python

### API:

######data_loader.py 
     '''alternative importer from csv file to database optimized for python'''
     
######server.py
     '''generates a flask api for accessing selected information from the database'''

######client.py
     '''Tests the outputs from server.py'''

