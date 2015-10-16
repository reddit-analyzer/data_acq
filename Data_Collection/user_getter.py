import time

try:
    import praw
except ImportError:
    print "Praw library not found."

try:
    from csv_getter import csvSave
except ImportError:
    print "thread_getter.py not found or not in local directory."

def userData(list_items, subreddit_name):
    str_time = time.strftime('%m%d%y_%I%p', time.localtime())
    output_name = subreddit_name + "_users_" + str_time + ".csv"
    r = praw.Reddit(user_agent='blah')
    user_data = []
    for post in list_items:
        reddit_username = post.author._case_name
        user = r.get_redditor(reddit_username)
        date_created = user.created #unix time
        date_created = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(date_created))
        comment_karmas = user.comment_karma
        link_karmas = user.link_karma
        verified_email = user.has_verified_email
        gold = user.is_gold
        mod = user.is_mod
        user_data.append([reddit_username,
                          date_created,
                          unicode(comment_karmas),
                          unicode(link_karmas),
                          verified_email,
                          gold,
                          mod])
    csvSave(user_data, output_name)
    return user_data