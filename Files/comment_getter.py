import time
import re

#Logistics
#Throw error if praw library not installed.
try:
    import praw
except ImportError:
    print "Praw library not found."

#Throw error if bs4 and BeautifulSoup is not installed.
try:
    from bs4 import BeautifulSoup
except ImportError:
    print "bs4 and BeautifulSoup library not found."

#Throw error if thread_getter/comment_getter library not found.
#Thread_getter and comment_getter must be in same directory as all_getter.
try:
    from csv_getter import csvSave
except ImportError:
    print "thread_getter.py not found or not in local directory."

#Comments data
def commentData(comments_list, now_time, subreddit_name):
    str_time = time.strftime('%m%d%y_%I%p', time.localtime())
    output_name = subreddit_name + "_comment_" + str_time + ".csv"
    if subreddit_name == "fp":
        front_page = 1
    else:
        front_page = 0
    now_time = now_time
    comment_data = []

    counter = 1
    for thread_comments in comments_list:
        print "subreddit: ", subreddit_name, "; counter: ", counter
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
                edited = str(comment_object.edited)
                if edited != "False":
                    edited = "True"
                comment_position = position
                length_comment = len(cleaned_comment)
                num_replies = len(comment_object.replies)
                comment_data.append([unicode(front_page),
                             thread_id,
                             comment_id,
                             comment_usr,
                             usr_id,
                             unicode(comment_upvotes),
                             cleaned_comment,
                             unicode(comment_position),
                             unicode(length_comment),
                             unicode(num_replies),
                             unicode(edited),
                             unicode(comment_gilds),
                             comment_created,
                             now_time])
            except:
                pass
            position += 1
        counter += 1
    csvSave(comment_data, output_name)
    return comment_data

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

    cleantext = BeautifulSoup(new_html, "html.parser").text
    pattern = "\n"
    originaltext = re.sub(pattern, "", cleantext).strip()
    return originaltext


