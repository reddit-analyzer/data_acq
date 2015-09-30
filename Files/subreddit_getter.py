#Throw error if all_getter file not found.
try:
    from all_getter import *
except ImportError:
    print "all_getter file not found."

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

#save_dir = "/Users/vincentpham/Google Drive/subreddit_got_files/test_folder"
subredditData("all")
