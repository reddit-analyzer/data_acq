import psycopg2
import matplotlib.pyplot as plt

def plot_common_phrases(password):
    try:
        conn = psycopg2.connect("dbname='reddit' user='postgres' host='localhost' password='" + password + "'")
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()

    query = " create temp table tmp as " + \
	"select distinct on(comment_id) comment_id, cleaned_comment, lower(cleaned_comment) as cleaned_comment2, comment_upvotes, comment_position " + \
	"from redditproject.comments " + \
	"ORDER BY COMMENT_ID, NOW_TIME DESC;"

    cur.execute(query)

    query1 = "select count(cleaned_comment2), avg(comment_upvotes) as avg_upvotes, cleaned_comment2 from tmp group by cleaned_comment2 order by 1 desc limit 20;"

    cur.execute(query1)
    select = cur.fetchall()
    count_comments = [x[0] for x in select]
    count_comments = count_comments[0:12] + count_comments[13:]

    avg_upvotes = [x[1] for x in select]
    avg_upvotes = avg_upvotes[0:12] + avg_upvotes[13:]

    comments = [x[2] for x in select]
    comments = comments[0:12] + comments[13:]

    #top20 = output[0:20]

    colors = ["red"] + ["teal"]*18
    colors[3] = "orange"

    fig, ax = plt.subplots()
    ax.scatter(count_comments, avg_upvotes, color = colors, alpha = .5, s = 200)

    for i, txt in enumerate(comments):
        ax.annotate(txt, (count_comments[i],avg_upvotes[i]))
    plt.title("Popular Sayings")
    plt.xlabel("Count of phrases")
    plt.ylabel("Average upvotes")

    plt.show()
    conn.close()
    return

