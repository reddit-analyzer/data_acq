setwd("/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis")
library(ggplot2)
library(car)
library(MASS)
library(hexbin)

#########################################################################################
#Length of Comment
data = read.csv("length_upvotes.csv", header = F)
data_subset = subset(data, V2 > 0)

#hex graph
with(data_subset, 
     smoothScatter(log(V1), log(V2), main="Scatterplot Colored by Smoothed Densities",
                   xlab = "Log of Number of Characters",
                   ylab = "Log of Upvotes"))

#create scatterplot
scatterplot(log(V2)~log(V1), data = data,
            boxplot = F, spread = F, smooth = F,
            xlab = "Length of Comment (Characters)", ylab = "Upvotes", main = "Comments")

ggplot(data_subset,aes(x=(V1),y=(V2))) + stat_binhex()

ggplot(data_subset,aes(x=log(V1),y=(V2))) + geom_point(alpha = 0.1)

ggplot(data_subset,aes(log(data_subset$V1))) + 
  geom_histogram(binwidth = 0.40, aes(y = ..density..), color = "blue", fill = "lightblue") +
  geom_density(color="blue") +
  xlab("Log of Number of Characters") +
  ylab("Density") +
  ggtitle("Distribution of Most Common Length of Comment") +
  theme(axis.text.x=element_text(colour="black"), axis.text.y=element_text(colour="black")) +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank())

#bubble plot
ggplot(data, aes(x=log(V1), y=V2)) +
  geom_point(aes(size=V3), fill = NA, shape = 1) +
  scale_size_continuous(range=c(2,15)) +
  theme(legend.position = "none")

#########################################################################################
#Subreddit bubble plot/popular subreddit
data1 = read.csv("subreddit.csv", header = F)

radius <- data1$V2/100
symbols(data1$V1, data1$V3, circles = radius)

#Most popular subreddit
#Ordered histogram IMPORTANT
V1_table <- table(data1$V1)
V1_levels <- names(V1_table)[order(-1*V1_table)]
data1$V1order <- factor(data1$V1, levels = V1_levels)
# Just to be clear, the above line is no different than:
# mtcars$cyl2 <- factor(mtcars$cyl, levels = c("6","4","8"))
# You can manually set the levels in whatever order you please. 
ggplot(data1, aes(x = V1order)) + 
  geom_bar(color = "blue", fill = "lightblue2") +
  stat_bin(aes(y=..count.., label=..count..), geom="text", hjust = -0.5) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5)) +
  theme(plot.title = element_text(size=30,lineheight=.8, 
                                  vjust=1)) +
  xlab("Subreddit") +
  ylab("Count") +
  ggtitle("Most Popular Subreddit on Front Page") +
  coord_flip() +
  theme(axis.text.x=element_text(colour="black"), axis.text.y=element_text(colour="black")) +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank())

#counts of subreddit occurrences in front page
library(plyr)
test = count(data1, "V1")

#########################################################################################
#density of comments vs time
data2 = read.csv("comments_time.csv", header = FALSE)
as.



