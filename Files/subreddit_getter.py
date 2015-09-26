#Throw error if all_getter file not found.
try:
    from all_getter import *
except ImportError:
    print "all_getter file not found."


def subredditData(subreddits_list = "all"):
    if subreddits_list == 1:
        chunks = ["fp", "worldnews", "aww"]
    elif subreddits_list == 2:
        chunks = ["todayilearned", "mildlyinteresting", "Showerthoughts"]
    elif subreddits_list == "all":
        chunks = ["fp", "worldnews", "aww",
                  "todayilearned", "mildlyinteresting", "Showerthoughts"]
    elif type(subreddits_list) == list:
        chunks = subreddits_list
    else:
        print "You can only pass in 1, 2, 'all', or a list of subreddits"
        return

    for subreddit in chunks:
        submissionData(subreddit)
        print "finished " + subreddit
    print "ALL DONE!"
    return

