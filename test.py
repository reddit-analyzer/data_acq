__author__ = 'vincentpham'
import praw
import time
import re
from bs4 import BeautifulSoup


#Comments data
def commentData(subreddit_name = "aww", limit = 25):
    praw_reddit = praw.Reddit(user_agent='blah')
    if subreddit_name == "front page":
        submissions = praw_reddit.get_front_page(limit = limit)
    else:
        submissions = praw_reddit.get_subreddit(subreddit_name).get_hot(limit=limit)
    comments_list = [x.comments for x in submissions]
    rows = []
    for thread_comments in comments_list:
        position = 1
        for comment_object in thread_comments:
            try:
                thread_id = comment_object._submission.id
                comment_str = comment_object.body_html #Get Comment
                cleaned_comment = clean_html(comment_str)
                comment_id = comment_object.id
                comment_usr = comment_object.author._case_name #Get User\
                usr_id = comment_object.author.id
                comment_upvotes = comment_object.score #Number of upvotes
                #comment_subreddit_id = comment_object.subreddit_id
                #comment_subreddit = comment_object.subreddit
                comment_gilds = comment_object.gilded
                #comment_epoch_time = comment_object.created
                comment_created = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(comment_object.created))
                now_time = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime())
                edited = comment_object.edited
                comment_position = position
                length_comment = len(cleaned_comment)
                rows.append([thread_id, comment_id,comment_usr, usr_id,
                         comment_upvotes, cleaned_comment, position,
                         length_comment, edited,comment_gilds,
                         comment_created, now_time])
            except:
                pass
            position += 1
    return rows

def clean_html(html_text):
    new_html = html_text
    while("<blockquote>" in new_html):
        try:
            block_start = new_html.index("<blockquote>")
            str_len = len("</blockquote>")
            block_end = new_html.index("</blockquote>")
            new_html = new_html[0:block_start] + new_html[block_end+str_len:-1]
        except:
            new_html = html_text

    cleantext = BeautifulSoup(new_html).text
    pattern = "\n"
    originaltext = re.sub(pattern, "", cleantext).strip()
    return originaltext
