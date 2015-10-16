COPY (SELECT length_comment, comment_upvotes, comment_position
	  FROM redditproject.comments
	  WHERE fp = '1') 
	  To '/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/length_upvotes.csv' 
	  WITH CSV;

COPY (SELECT subreddit_name, num_posts, post_score, fp
	  FROM redditproject.threads
	  WHERE fp = '1') 
	  To '/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/subreddit.csv' 
	  WITH CSV;

COPY (SELECT length_comment, comment_upvotes, comment_position, comment_created
	  FROM redditproject.comments
	  WHERE fp = '0'
	  ORDER BY comment_created)
	  To '/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/comments_time.csv'
	  WITH CSV;

COPY (SELECT cleaned_comment 
	  FROM redditproject.comments)
	  To '/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/comments4graph.csv'
	  WITH CSV;

COPY (SELECT domain_name, subreddit_name 
	  FROM redditproject.threads
	  WHERE fp = '0')
	  To '/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/domain4graph.csv'
	  WITH CSV;
