import praw
import time
from thread_getter import *
from comment_getter import *
def submissionData(subreddit_name = 'aww'):
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

    threadData(list_items, now_time, subreddit_name = subreddit_name)
    commentData(comment_lists, now_time, subreddit_name = subreddit_name)
    return

