set search_path = 'redditproject';

select * from threads limit 100;
select * from comments limit 100;

select distinct(subreddit_name) from threads;
select distinct on(thread_id) count(*) from threads where subreddit_name = 'worldnews' group b;

create temp table tmp as
	select b.*
	from (select distinct thread_id 
		from threads
		where subreddit_name = 'worldnews') a
	left join (select * from threads) b
	using(thread_id);


select distinct thread_id, domain_name from threads where subreddit_name = 'worldnews';

select domain_name, count(domain_name) as cnt from threads where subreddit_name = 'worldnews' group by domain_name
	order by cnt desc;


--GET DOMAIN NAMES FOR WORLDNEWS
create temp table tmp1 as 
	select distinct thread_id, domain_name, post_title from threads
	where subreddit_name = 'worldnews';

select domain_name, count(domain_name) as cnt from tmp1
	group by domain_name
	order by cnt desc;

select count(*) from tmp1; --168

--GET DOMAIN NAMES FOR NOTTHEONION
create temp table tmp2 as 
	select distinct thread_id, domain_name, post_title from threads
	where subreddit_name = 'nottheonion';

select domain_name, count(domain_name) as cnt from tmp2 
	group by domain_name
	order by cnt desc;

select count(*) from tmp2; --152

--playing around with news
select post_title from tmp1 where domain_name = 'theguardian.com' order by post_title;
select post_title from tmp2 where domain_name = 'theguardian.com' order by post_title;

drop table tmp2;

select count() from comments where cleaned_comment ilike '%repost%';

select domain_name, count(domain_name) as cnt from threads where subreddit_name = 'nottheonion' group by domain_name
	order by cnt desc;

select * from 

select distinct on(thread_id) * from threads where subreddit_name = 'worldnews' group by thread_id;

select count(*) from threads; --1900
select count(distinct thread_id) from threads; --958

-- EMOTICONS 

select distinct comment_id, cleaned_comment from comments where cleaned_comment like '%:)%';
select distinct comment_id from comments where cleaned_comment like '%:(%';
select distinct comment_id from comments where cleaned_comment like '%:D%';
select distinct comment_id, cleaned_comment from comments where cleaned_comment like '%XD%';
select distinct comment_id, cleaned_comment from comments where cleaned_comment like '%:|%';
 >_<

 -- TOP COMMENTS --24638
 create temp table tmp as 
	select distinct on(comment_id) comment_id, cleaned_comment, lower(cleaned_comment) as cleaned_comment2, comment_upvotes, comment_position
	from comments
	ORDER BY COMMENT_ID, NOW_TIME DESC;

select count(cleaned_comment), avg(comment_upvotes) as avg_upvotes, avg(comment_position) as avg, cleaned_comment from tmp group by cleaned_comment order by 1 desc;
select count(cleaned_comment2), avg(comment_upvotes) as avg_upvotes, avg(comment_position) as avg, cleaned_comment2 from tmp group by cleaned_comment2 order by 1 desc;

select count(cleaned_comment) from tmp where cleaned_comment ilike '%repost%';

drop table tmp;


---------Join the two tables
--validation
select count(*) from comments a
	left join threads b
	on a.thread_id = b.thread_id and date_part('hour', a.now_time) = date_part('hour', b.now_time)
		and date_part('day', a.now_time) = date_part('day', b.now_time)
	where subreddit_name is not null;

-- analyze comments for where the thread was rank = 1
select a.*, b.rank from comments a
	left join threads b
	on a.thread_id = b.thread_id and date_part('hour', a.now_time) = date_part('hour', b.now_time)
		and date_part('day', a.now_time) = date_part('day', b.now_time)
	where subreddit_name is not null and b.rank = 1;

--get top level comments and all comments count for a thread (grouped by num_comments to specify unique time)
select thread_id, count(thread_id), num_comments, now_time
	from (select a.*, b.rank from comments a
		right join threads b
		on a.thread_id = b.thread_id and date_part('hour', a.now_time) = date_part('hour', b.now_time)
			and date_part('day', a.now_time) = date_part('day', b.now_time)
		where subreddit_name is not null and b.rank = 1) as inner_query
	group by thread_id, num_comments, now_time;

--playing with time
select ranking, now_time - post_time + interval '7 hours' from threads where fp = '1';
select 

--playing with candidates
select count(distinct cleaned_comment) from comments where cleaned_comment ilike '%trump%';
select count(distinct cleaned_comment) from comments where cleaned_comment ilike '%obama%';
select count(distinct cleaned_comment) from comments where cleaned_comment ilike '%hilary%';
select count(distinct cleaned_comment) from comments where cleaned_comment ilike '%sanders%';

select politicians, count(politicians) as cnt
	from (select distinct cleaned_comment, (case when cleaned_comment ilike '%trump%' then 'Trump' 
			when cleaned_comment ilike '%obama%' then 'Obama'
			when cleaned_comment ilike '%clinton%' then 'Clinton'
			when cleaned_comment ilike '%sanders%' then 'Sanders'
			ELSE NULL END) AS POLITICIANS
		FROM COMMENTS) as inner_query
	where politicians is not null
	group by politicians
	order by cnt desc;

select distinct cleaned_comment from comments where cleaned_comment ilike '%trump%' and cleaned_comment not ilike '%nazi%';
select distinct cleaned_comment from comments where cleaned_comment ilike '%obama%';

--playing with city
select distinct cleaned_comment from comments where cleaned_comment ilike '%san francisco%';
select distinct cleaned_comment from comments where cleaned_comment ilike '%chicago%';
select distinct cleaned_comment from comments where cleaned_comment ilike '%new york%';

--playing with sports
select sportss, count(sportss) as cnt
	from (select distinct cleaned_comment, (case when cleaned_comment ilike '%baseball%' then 'baseball' 
			when cleaned_comment ilike '%football%' then 'football'
			when cleaned_comment ilike '%soccer%' then 'soccer'
			when cleaned_comment ilike '%hockey%' then 'hockey'
			ELSE NULL END) AS sportsS
		FROM COMMENTS) as inner_query
	where sportss is not null
	group by sportss
	order by cnt desc;

--checking distrubiton of comments
select max(length_comment) from comments;
select min(length_comment) from comments;
select avg(length_comment) from comments;

select max(length_comment)
	from (select length_comment, ntile(2) over (partition by null order by length_comment) as halves
		from comments) as inner_query
	where halves = 1;