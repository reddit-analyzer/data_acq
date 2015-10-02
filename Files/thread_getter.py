import time

try:
    from csv_getter import csvSave
except ImportError:
    print "thread_getter.py not found or not in local directory."

def threadData(list_items, now_time, subreddit_name):
    str_time = time.strftime('%m%d%y_%I%p', time.localtime())
    output_name = subreddit_name + "_thread_" + str_time + ".csv"
    if subreddit_name == "fp":
        front_page = 1
    else:
        front_page = 0
    thread_data = []

    ranking = 0
    now_time = now_time
    for post in list_items:
        subreddit_name = post.subreddit._case_name
        reddit_usernames = post.author._case_name
        post_title = post.title
        post_text = post.selftext
        total_num_comments = post.num_comments
        post_timestamp_tmp = post.created
        post_timestamp_final = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(post_timestamp_tmp))
        domains = cleanDomain(post.domain)
        gilded_score = post.gilded
        post_score = post.score
        thread_ids = post.id #matched with comment's domain called _submission_id
        post_url = post.url
        ranking += 1
        thread_data.append([unicode(front_page),
                            subreddit_name,
                            reddit_usernames,
                            post_title,
                            post_text,
                            thread_ids,
                            unicode(total_num_comments),
                            domains,
                            unicode(gilded_score),
                            unicode(post_score),
                            unicode(ranking),
                            post_timestamp_final,
                            now_time,
                            post_url])
    csvSave(thread_data, output_name)
    return thread_data

def cleanDomain(domain_name):
    if 'self.' in domain_name:
        mapped_name = 'reddit.com'
        return mapped_name
    else:
        return domain_name

