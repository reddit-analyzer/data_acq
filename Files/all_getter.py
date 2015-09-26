#Main function to call to get comment data and thread data from Reddit.com

'''This script can be called to crawl and scrape data from Reddit.com using
the praw library. Both thread_getter.py and comment_getter.py must be
present in the same folder or directory as this script.'''

import time

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


def submissionData(subreddit_name):
    r = praw.Reddit(user_agent='blah')
    if subreddit_name == "fp":
        submissions = r.get_front_page()
    else:
        submissions = r.get_subreddit(subreddit_name).get_hot()


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

