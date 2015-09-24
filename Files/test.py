<<<<<<< HEAD
import praw
import time
import csv
import re
=======
__author__ = 'vincentpham'
import praw
import time

>>>>>>> 1d0a2957910f479630465146050acfc2b876e927

#Comments data
r = praw.Reddit(user_agent='blah')
submissions = r.get_subreddit('aww').get_hot(limit=1)


y = [x.comments for x in submissions]

for x in submissions:
    y = x

comment_object = y[0][0]
comment_str = comment_object.body #Get Comment
comment_usr = comment_object.author._case_name #Get User\
comment_upvotes = comment_object.score #Number of upvotes
comment_subreddit_id = comment_object.subreddit_id
comment_subreddit = comment_object.subreddit
comment_gilds = comment_object.gilded
comment_epoch_time = comment_object.created
comment_created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r.created))
comment_edited = comment_object.edited

e = [str(x) for x in submissions]

for x in submissions:
    print x

user = r.get_redditor('ketralnis')
user.link_karma
user.comment_karma

user.fullname

s = r.get_submission('http://www.reddit.com/r/redditdev/comments/s3vcj/_/c4axeer')
your_comment = s.comments[0]


#thread data:
r = praw.Reddit(user_agent='blah')
submissions = r.get_subreddit('aww').get_hot(limit=1)

<<<<<<< HEAD
subreddit_name = 'aww'
def threadData(subreddit_name = 'aww', limit = 25):
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
    csvSave(thread_data)
    return thread_data

def cleanDomain(domain_name):
    if 'self.' in domain_name:
        mapped_name = 'reddit.com'
        return mapped_name
    else:
        return domain_name

def csvSave(list_of_list):
    result_csv = open("testredditdata.csv", "w")
    content = csv.writer(result_csv)#, delimiter = ',', quoting = csv.QUOTE_NONE, quotechar = '', lineterminator='\r\n')
    for item in list_of_list:
        content.writerow(item)
    result_csv.close()
    return "Saved"

test = threadData('aww')

#y = [x.comments for x in submissions]

y = []
for x in submissions:
    y.append(x)

#REDDIT_USERNAME
for item in y:
    try:
        print item.author._case_name
    except:
        print "DELETED"

#TOTAL COMMENTS
for item in y:
    try:
        print item.num_comments
    except:
        print "DELETED"

#POST TIMESTAMP
for item in y:
    try:
        print item.created
    except:
        print "DELETED"

#SOURCE or DOMAIN
for item in y:
    try:
        print item.domain
    except:
        print "DELETED"

#GILDED
for item in y:
    try:
        print item.gilded
    except:
        print "DELETED"

#SCORE
for item in y:
    try:
        print item.score
    except:
        print "DELETED"

#THREAD ID
for item in y:
    try:
        print item.id
    except:
        print "DELETED"
=======

y = [x.comments for x in submissions]

for x in submissions:
    y = x
>>>>>>> 1d0a2957910f479630465146050acfc2b876e927

author = y.author._case_name
created = y.created
domain = y.domain
edit_time = y.edited
gilded = y.gilded

media = y.media
media_embedded = y.media_embed #?
num_comments = y.num_comments
score = y.score
secured_media = y.secured_media #?
secure_media_embed = y.secure_media_embed
text = y.selftext_html
stickied = y.stickied
subreddit_name = y.subreddit._case_name
subreddit_id = y.subreddit_id
title = y.title
url = y.url

<<<<<<< HEAD
string_test = u'hello\nbye'

# test = re.sub(r'<[^>]blockquote>*<[^>]/blockquote>','', str(string_test))
test = re.sub(r'\n','', str(string_test))
=======
>>>>>>> 1d0a2957910f479630465146050acfc2b876e927
