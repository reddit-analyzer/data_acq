__author__ = 'vincentpham'
from flask import Flask, request, jsonify
import psycopg2, psycopg2.extras
import collections
import re


DB_DSN = '''host=db.cvu5a6kuxniq.us-west-2.rds.amazonaws.com 
            dbname=db_restaurants user=dbuser password=dbpassword'''

HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def home():
    '''
    :return: home message
    '''
    output = dict()

    output['message'] = "Welcome to the Reddit Project Homepage"
    return jsonify(output)

@app.route('/help')
def help():
     '''
    :return: json dict of urls to use
    '''
    output = dict()

    output['a'] = '/counts/<table>/total'
    output['b'] = '/counts/<table>/subreddit'
    output['c'] = '/counts/word/<word>'
    output['d'] = '/subreddit/mostlikely/<word>'
    output['e'] = '/<table>/dates'
    output['f'] = '/topcommenters/<number>'
    output['g'] = '/topcommenters/<subreddit>/<number>'
    output['h'] = '/u/<user_name>'
    output['i'] = '/u/<user_name>/stats'
    output['j'] = '/links/<word>/<number>'
    output['k'] = '/popularwords/subreddit/<number>'

    return jsonify(output)


@app.route('/counts/<table>/total')
def count_table_records(table):
    """
    calculates the total number of records collected
     in the threads or comments table
    :param table: name of table ("comments" or "threads") to query
    :return: a json dict of all kv pairs, key = table and value = count
    """
    out = dict()
    try:
        if table == "threads":
            query = "select count(*) as cnt from threads;"
        elif table == "comments":
            query = "select count(*) as cnt from comments;"
        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        rs = cur.fetchone()
        out[table] = rs["cnt"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()
    return jsonify(out)

@app.route('/counts/<table>/subreddit')

def count_subreddit(table):
    """
    calculates the total number of records per subreddit collected
     in the threads or comments table
    :param table: name of table ("comments" or "threads") to query
    :return: a json dict of all kv pairs, key = subreddit and value = count
    """
    out = dict()
    try:
        if table == "threads":
            query = '''select subreddit_name, count(subreddit_name) as cnt 
                        from threads
                        group by subreddit_name order by cnt desc;'''
        if table == "comments":
            query = '''select subreddit_name, count(subreddit_name) as cnt 
                        from comments a
                        left join threads b
                        on a.thread_id = b.thread_id and
                    date_part('hour', a.now_time) = date_part('hour', b.now_time)
                    and date_part('day', a.now_time) = date_part('day', b.now_time)
                    where subreddit_name is not null
                    group by subreddit_name;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        rs = cur.fetchall()
        for row in rs:
            key = row["subreddit_name"]
            out[key] = row["cnt"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/counts/word/<word>')

def count_word(word):
    """
    calculates the total number of times a given word appears in the comments 
    :param word: (str) any word or str of interests
    :return: a dict of all kv pairs, key = word and value = count
    """
    out = dict()

    try:
        query = '''select count(cleaned_comment) as cnt FROM comments
                    where cleaned_comment ilike %(like)s;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query,dict(like= '%'+word+'%')) #to include 
        cur.execute(m_query)
        rs = cur.fetchone()
        out[word] = rs["cnt"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)


@app.route('/subreddit/mostlikely/<word>')

def get_likely_subreddit(word):
    """
    Obtains the most likely subreddit with the given word by word count
    :param word: (str) any word or str of interests
    :return: a dict of all kv pairs, key = subreddit and value = count
    """
    out = dict()

    try:
        query = '''select subreddit_name, count(subreddit_name) as cnt 
                    from comments a
                    left join threads b
                    on a.thread_id = b.thread_id and
                    date_part('hour', a.now_time) = date_part('hour', b.now_time)
                        and date_part('day', a.now_time) = date_part('day', b.now_time)
                    where subreddit_name is not null
                        and cleaned_comment ilike %(like)s
                    group by subreddit_name
                    order by cnt desc;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query,dict(like= '%'+word+'%'))
        cur.execute(m_query)
        rs = cur.fetchone()
        out[rs["subreddit_name"]] = rs["cnt"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/<table>/dates')

def get_dates_record(table):
    """
    calculates the total number of records in a given table by date
    :param table: name of table ("comments" or "threads") to query
    :return: a dict of all kv pairs, key = date and value = count
    """
    out = dict()
    try:
        if table == "threads":
            query = '''select dates, count(dates) as cnt
                        from (select now_time::date as dates from threads)
                        as inner_query
                        group by dates
                        order by dates'''

        if table == "comments":
            query = '''select dates, count(dates) as cnt
                        from (select now_time::date as dates from comments)
                        as inner_query
                        group by dates
                        order by dates'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        rs = cur.fetchall()
        for row in rs:
            key = str(row["dates"])
            out[key] = row["cnt"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)


@app.route('/topcommenters/<number>')

def get_topcommenters(number):
    """
    Calculates the top n users who post comments
    :param number: amount of users interested in pulling
    :return: a dict of all kv pairs, key = user and value = count
    """
    out = dict()
    try:
        query = '''select comment_usr, count(comment_usr) as cnt from comments
                    group by comment_usr
                    order by cnt desc
                    limit %s;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query, (number,))
        cur.execute(m_query)
        rs = cur.fetchall()
        for row in rs:
            key = row["comment_usr"]
            out[key] = row["cnt"]
    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/topcommenters/<subreddit>/<number>')

def get_topcommenters_subreddit(subreddit,number):
    """
    Calculates the top n users who post comments for a given subreddit
    :param subreddit: name of subreddit (e.g: "aww", "worldnews) interested in
    :param number: amount of users interested in pulling
    :return: a dict of all kv pairs, key = user and value = count
    """
    out = dict()
    try:
        query = '''select comment_usr, count(comment_usr) as cnt 
                    from comments a
                    inner join threads b
                    on a.thread_id = b.thread_id and
                    date_part('hour', a.now_time) = date_part('hour', b.now_time)
                        and date_part('day', a.now_time) = date_part('day', b.now_time)
                    where subreddit_name = %s
                    group by comment_usr
                    order by cnt desc
                    limit %s;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query, (subreddit, number,))
        cur.execute(m_query)
        rs = cur.fetchall()
        for row in rs:
            key = row["comment_usr"]
            out[key] = row["cnt"]
    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/u/<user_name>') #used /u to keep consistent with Reddit format

def get_user_data(user_name): 
    """
    Return all comments posted for a given user with related information
    :param user_name: name of user interested in pulling data from
    :return: a dict of all kv pairs with value as list of kv, key = comment_id 
        and value = [{'subreddit':subreddit},{'upvotes':count},
                     {'created':date posted},{'comment': comment posted}]
    """
    out = dict()
    try:
        query = '''select distinct on(comment_id) comment_id, comment_upvotes,
                    cleaned_comment, subreddit_name, comment_created
                    from comments a
                    inner join threads b
                    on a.thread_id = b.thread_id and
                    date_part('hour', a.now_time) = date_part('hour', b.now_time)
                        and date_part('day', a.now_time) = date_part('day', b.now_time)
                    where comment_usr = %s
                    order by comment_id, comment_created desc;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query, (user_name,))
        cur.execute(m_query)

        rs = cur.fetchall()
        for row in rs:
            key = row["comment_id"]
            out[key] = [{'subreddit': row["subreddit_name"]},
                        {'upvotes': row["comment_upvotes"]},
                        {'created': row["comment_created"]},
                        {'comment': row["cleaned_comment"]}]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)


@app.route('/u/<user_name>/stats') #used /u to keep consistent with Reddit format

def get_user_stats(user_name): 
    """
    Return states for a given user
    :param user_name: name of user interested in pulling data from
    :return: a dict of all kv pairs, key = stats_type and value = stats
    """
    out = dict()
    try:
        query = '''select sum(comment_upvotes)/count(comment_upvotes) as avg_upvotes,
                        max(comment_upvotes) as max_upvotes,
                        min(comment_upvotes) as min_upvotes,
                        sum(comment_upvotes) as total_upvotes,
                        count(comment_upvotes) as total_posts,
                        sum(comment_gilds) as total_gold
                    from comments
                    where comment_usr = %s;'''

        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query, (user_name,))
        cur.execute(m_query)
        rs = cur.fetchone()
        out["Average Karma"] = rs["avg_upvotes"]
        out["Lowest Karma"] = rs["min_upvotes"]
        out["Highest Karma"] = rs["max_upvotes"]
        out["Total Karma"] = rs["total_upvotes"]
        out["Total Posts"] = rs["total_posts"]
        out["Total Gold"] = rs["total_gold"]

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/links/<word>/<number>')

def get_related_links(word, number):
    """
    Calculates n link related to a given word sorted by post score
    :param word: word or phrases interested in getting links for
    :param number: amount of links to pull
    :return: a dict of all kv pairs with value as list of kv, key = link number 
        and value = [{'Post Title':title},{'url':url},]"""
    out = dict()
    try:
        query = '''select distinct on(thread_id) thread_id, post_title,
                    post_score, post_url
                    from threads
                    where post_url IS NOT null
                        and post_title ilike %(like)s
                    order by thread_id, post_score desc
                    limit %(total)s;
                '''
        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        m_query = cur.mogrify(query, dict(like= '%'+word+'%',total=number))
        cur.execute(m_query)
        rs = cur.fetchall()
        counter = 1
        for row in rs:
            link_key = "link" + str(counter)
            out[link_key] = [{'Post Title': row["post_title"]},
                             {"url": row["post_url"]}]
            counter += 1

    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

@app.route('/popularwords/subreddit/<number>')

def get_popularwords(number):
    """
    calculates the n most popular word by subreddit
    :param number: amount of popular words to pull per subreddit
    :return: a dict of all kv pairs, key = subreddit and value = {word : count}
    """
    all_counts = dict()
    out = dict()
    try:
        query = '''select distinct
                    cleaned_comment, subreddit_name
                    from comments a
                    inner join threads b
                    on a.thread_id = b.thread_id and
                    date_part('hour', a.now_time) = date_part('hour', b.now_time)
                        and date_part('day', a.now_time) = date_part('day', b.now_time)
                    where cleaned_comment is not null;
                '''
        conn = psycopg2.connect(dsn=DB_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)

        punctuations = [".","?","!",")","(",";",":",","," - ",
                        "'","\\", "\"", "for", " are", " her ", " his " ,
                        "the", "was", "but", "and", "you", " he ", " she ",
                        "that", "this", "like", "have", "with", "just"]
        rs = cur.fetchall()

        for row in rs:
            subreddit = row["subreddit_name"]
            comments = row["cleaned_comment"]
            comments = comments.lower()

            for punc in punctuations:
                comments = comments.replace(punc, " ")
            comments = re.sub(r'\b\w{1,2}\b', '', comments)

            if subreddit in all_counts:
                all_counts[subreddit].update(comments.split())
            else:
                all_counts[subreddit] = collections.Counter(comments.split())

        for x in all_counts:
            popular = all_counts[x].most_common(int(number))
            out[x] = [{y[0]:y[1]} for y in popular]
    except psycopg2.Error as e:
        print e.message
    else:
        cur.close()
        conn.close()

    return jsonify(out)

if __name__ == '__main__':
    app.debug = False # only have this on for debugging!
    app.run(host=HOST) # need this to access from the outside world!

