__author__ = 'vincentpham'
import praw
import time


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


y = [x.comments for x in submissions]

for x in submissions:
    y = x

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

