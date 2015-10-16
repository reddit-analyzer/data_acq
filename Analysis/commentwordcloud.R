library(wordcloud)

setwd("/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/")
data = read.table("comments4graph.txt")

wordcloud(data, scale=c(5,0.5), max.words=100, random.order=FALSE, 
          rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))