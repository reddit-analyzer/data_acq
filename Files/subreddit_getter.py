'''This script can be called to crawl and scrape data from Reddit.com using
the praw library. Both thread_getter.py and comment_getter.py must be
present in the same folder or directory as this script.'''
#Logistics

#Throw error if praw library not installed.
try:
    import praw
except ImportError:
    print "Praw library not found."

#Throw error if thread_getter/comment_getter library not found.
#Thread_getter and comment_getter must be in same directory as all_getter.
try:
    from thread_getter import *
except ImportError:
    print "thread_getter.py not found or not in local directory."

try:
    from comment_getter import *
except ImportError:
    print "comment_getter.py not found or not in local directory."

import os

def subredditData(subreddits_list = "all", save_dir = None, limit = 0):

    if save_dir != None:
        os.chdir(save_dir)

    if subreddits_list == 1:
        chunks = ["fp", "worldnews", "aww"]
    elif subreddits_list == 2:
        chunks = ["nottheonion", "television", "AnimalsBeingJerks"]
    elif subreddits_list == "all":
        chunks = ["fp", "worldnews", "aww",
                  "nottheonion", "television", "AnimalsBeingJerks"]
    elif type(subreddits_list) == list:
        chunks = subreddits_list
    else:
        print "You can only pass in 1, 2, 'all', or a list of subreddits"
        return

    for subreddit in chunks:
        submissionData(subreddit, limit = limit)
        print "finished " + subreddit
    print "ALL DONE!"
    return

<<<<<<< HEAD
#save_dir = "/Users/vincentpham/Google Drive/subreddit_got_files/test_folder"
subredditData("all")
=======
def submissionData(subreddit_name, limit = 0):
    r = praw.Reddit(user_agent='blah')
    if subreddit_name == "fp":
        submissions = r.get_front_page(limit = limit)
    else:
        submissions = r.get_subreddit(subreddit_name).get_hot(limit = limit)


    now_time = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())

    sub_lists = [x for x in submissions]
    list_items = []
    for x in sub_lists:
        if not x.stickied:
            list_items.append(x)

    comment_lists = []
    for x in list_items:
        comment_lists.append(x.comments)

    threadData(list_items, now_time, subreddit_name)
    commentData(comment_lists, now_time, subreddit_name)
    return

#save_dir = "/Users/vincentpham/Google Drive/subreddit_got_files/test_folder"
#subredditData(2, save_dir)
>>>>>>> 241cd554e05e7d113d7b85f5a5934eb0963df6c6
