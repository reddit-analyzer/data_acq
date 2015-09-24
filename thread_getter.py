import praw
import time
import csv
import re

def threadData(subreddit_name = 'aww', limit = 25, output_name = "testredditdata.csv"):
    #subreddit = r.get_subreddit(subreddit_name)
    r = praw.Reddit(user_agent='blah')
    submissions =  r.get_subreddit(subreddit_name).get_hot(limit = limit)
    list_items = [item for item in submissions]
    thread_data = []
    ranking = 0
    for post in list_items:
        subreddit_name = post.subreddit._case_name
        reddit_usernames = post.author._case_name
        total_num_comments = post.num_comments
        post_timestamp_tmp = post.created
        post_timestamp_final = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(post_timestamp_tmp))
        domains = cleanDomain(post.domain)
        gilded_score = post.gilded
        post_score = post.score
        thread_ids = post.id #matched with comment's domain called _submission_id
        now_time = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())
        ranking += 1
        thread_data.append([subreddit_name,
                            reddit_usernames,
                            thread_ids,
                            total_num_comments,
                            domains,
                            gilded_score,
                            post_score,
                            ranking,
                            post_timestamp_final,
                            now_time])
    csvSave(thread_data, output_name)
    return thread_data

def cleanDomain(domain_name):
    if 'self.' in domain_name:
        mapped_name = 'reddit.com'
        return mapped_name
    else:
        return domain_name

def csvSave(list_of_list, outfile):
    result_csv = open(outfile, "w")
    content = csv.writer(result_csv)#, delimiter = ',', quoting = csv.QUOTE_NONE, quotechar = '', lineterminator='\r\n')
    for item in list_of_list:
        content.writerow(item)
    result_csv.close()
    return "Saved"

test = threadData('aww')