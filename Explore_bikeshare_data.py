
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



system('python -m nbconvert Explore_bikeshare_data.ipynb')
