
library(dplyr)
library(ggplot2)
library(tidyverse)

ny = read.csv('new_york_city.csv')
wash = read.csv('washington.csv')
chi = read.csv('chicago.csv')

head(ny)

head(chi)

head(wash)

class(ny$Start.Time)

ny = read.csv(file='new_york_city.csv', stringsAsFactors = FALSE)

class(ny$Start.Time)

colSums(is.na(ny))

ny$Gender[ny$Gender==""] <-NA
ny$User.Type[ny$User.Type ==""] <-NA


colSums(is.na(ny))

# view Start.Time field
ny$Start.Time[1]

ny$Start.Time = as.POSIXct(ny$Start.Time, format = '%Y-%m-%d %H:%M:%S')
ny$Start.Time[1]

ny$month = format(ny$Start.Time, "%m")
ny$hour = format(ny$Start.Time, "%H")
head(ny)

MN <- ggplot(ny) + geom_bar(aes(x = month))

MN + ggtitle("the count of rents for each month")

HN <- ggplot(ny) + geom_bar(aes(x = hour))

HN + ggtitle("the count of rents for each Hour of day")

chi = read.csv(file='chicago.csv', stringsAsFactors = FALSE)

colSums(is.na(chi))

chi$Gender[chi$Gender==""] <-NA
chi$User.Type[chi$User.Type ==""] <-NA

colSums(is.na(chi))

chi$Start.Time = as.POSIXct(chi$Start.Time, format = '%Y-%m-%d %H:%M:%S')
chi$Start.Time[1]

chi$month = format(chi$Start.Time, "%m")
chi$hour = format(chi$Start.Time, "%H")
head(chi)

Mc <- ggplot(chi) + geom_bar(aes(x = month))

Mc + ggtitle("the count of rents for each month")

Hc <- ggplot(chi) + geom_bar(aes(x = hour))

Hc + ggtitle("the count of rents for each Hour of day")

wash = read.csv(file='washington.csv', stringsAsFactors = FALSE)

colSums(is.na(wash))

wash$Start.Time = as.POSIXct(wash$Start.Time, format = '%Y-%m-%d %H:%M:%S')
wash$Start.Time[1]

wash$month = format(wash$Start.Time, "%m")
wash$hour = format(wash$Start.Time, "%H")
head(wash)

MW <- ggplot(wash) + geom_bar(aes(x = month))

MW + ggtitle("the count of rents for each month")

HW <- ggplot(wash) + geom_bar(aes(x = hour))

HW + ggtitle("the count of rents for each Hour of day")

print(table(ny$month))
print(table(chi$month))
print(table(wash$month))

length(unique(ny$Start.Station))

top10_Start.Station <- sort(table(ny$Start.Station), decreasing = TRUE)
head(top10_Start.Station, n = 10)

length(unique(ny$End.Station))

top10_End.Station <- sort(table(ny$End.Station), decreasing = TRUE)
head(top10_End.Station, n = 10)

length(unique(chi$Start.Station))

top10_Start.Station <- sort(table(chi$Start.Station), decreasing = TRUE)
head(top10_Start.Station, n = 10)

length(unique(chi$End.Station))

top10_End.Station <- sort(table(chi$End.Station), decreasing = TRUE)
head(top10_End.Station, n = 10)

length(unique(wash$Start.Station))

top10_Start.Station <- sort(table(wash$Start.Station), decreasing = TRUE)
head(top10_Start.Station, n = 10)

length(unique(wash$End.Station))

top10_End.Station <- sort(table(wash$End.Station), decreasing = TRUE)
head(top10_End.Station, n = 10)

summary(ny$Trip.Duration)

ggplot(ny,aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  ylab('Number of riders')+
  ggtitle("Initial Histogram of Distribution of riders Trip Duration in NY")

ggplot(ny, aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  coord_cartesian(xlim=c(61,4000))+
  ylab('Number of riders')+
  ggtitle('Histogram of riders Trip Duration in NY with values between 61 and 4000')

summary(chi$Trip.Duration)

ggplot(chi,aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  ylab('Number of riders')+
  ggtitle("Initial Histogram of Distribution of riders Trip Duration in chi")

ggplot(chi, aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  coord_cartesian(xlim=c(60,6000))+
  ylab('Number of riders')+
  ggtitle('Histogram of riders Trip Duration in chi with values between 61 and 4000')

summary(wash$Trip.Duration)

ggplot(wash,aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  ylab('Number of riders')+
  ggtitle("Initial Histogram of Distribution of riders Trip Duration in wash")

ggplot(wash, aes(x= Trip.Duration))+
  geom_histogram(binwidth = 300, color = 'black', fill = '#099DD9')+
  coord_cartesian(xlim=c(60,7000))+
  ylab('Number of riders')+
  ggtitle('Histogram of riders Trip Duration in wash with values between 61 and 4000')


system('python -m nbconvert Explore_bikeshare_data.ipynb')
