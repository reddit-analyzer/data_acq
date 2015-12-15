__author__ = 'vincentpham'
import httplib

SERVER = '52.27.248.86:5000'

def get_data(directory, SERVER):
    '''Generic function for requesting for a
        given directory and SERVER
    return: the requested data
    '''
    h = httplib.HTTPConnection(SERVER)
    h.request('GET','http://' + SERVER + directory)
    resp = h.getresponse()
    return resp.read()

def home():
    return get_data("/", SERVER)

def count_table_records(table):
    directory = "/counts/" + table + "/total"
    return get_data(directory, SERVER)

def count_subreddit(table):
    directory = "/counts/" + table + "/subreddit"
    return get_data(directory, SERVER)

def count_word(word):
    directory = "/counts/word/" + word
    return get_data(directory, SERVER)

def get_likely_subreddit(word):
    directory = "/subreddit/mostlikely/" + word
    return get_data(directory, SERVER)

def get_dates_record(table):
    directory = "/" + table + "/dates"
    return get_data(directory, SERVER)

def get_topcommenters(number):
    directory = "/topcommenters/" + number
    return get_data(directory, SERVER)

def get_topcommenters_subreddit(subreddit, number):
    directory = "/topcommenters/" + subreddit + "/" + number
    return get_data(directory, SERVER)

def get_user_data(user_name):
    directory = "/u/" + user_name
    return get_data(directory, SERVER)

def get_user_stats(user_name):
    directory = "/u/" + user_name + "/stats"
    return get_data(directory, SERVER)

def get_related_links(word, number):
    directory = "/links/" + word + "/" + number
    return get_data(directory, SERVER)

def get_popularwords(number):
    directory = "/popularwords/subreddit/" + number
    return get_data(directory, SERVER)

if __name__ == '__main__':
    print "************************************************"
    print "test of my flask app running at ", SERVER
    print "created by Vincent Pham"
    print "************************************************"
    print " "
    print "******** home message **********"
    print home()
    print " "
    print "******** counts at table threads **********"
    print count_table_records('threads')
    print "******** counts at table comments **********"
    print count_table_records('comments')
    print " "
    print "*** counts at table threads per subreddit ***"
    print count_subreddit('threads')
    print "*** counts at table comments per subreddit ***"
    print count_subreddit('comments')
    print " "
    print "*** counts number of times cat was mentioned ***"
    print count_word("cat")
    print "*** counts number of times politician was mentioned ***"
    print count_word("politician")
    print " "
    print "***** Most likely subreddit where cat is mentioned *****"
    print get_likely_subreddit("cat")
    print "*** Most likely subreddit where politician is mentioned ***"
    print get_likely_subreddit("politician")
    print " "
    print "***** counts records for table threads per date *******"
    print get_dates_record("threads")
    print "***** counts records for table comments per date ******"
    print get_dates_record("comments")
    print " "
    print "******** Top 10 commenters **********"
    print get_topcommenters("10")
    print " "
    print "******** Top 10 commenters for the subreddit aww **********"
    print get_topcommenters_subreddit("aww", "10")
    print " "
    print "******** All comments by user HaikuberryFin **********"
    print get_user_data("HaikuberryFin")
    print " "
    print "******** Stats for user HaikuberryFin **********"
    print get_user_stats("HaikuberryFin")
    print " "
    print "******** 5 most popular links that referenced cats **********"
    print get_related_links("cats","5")
    print " "
    print "******** 4 most popular words per subreddit **********"
    print get_popularwords("4")
    print " "



