6+7*3/2

x <- 1:4
x

x2 <- x**2
x2

X <- 10
prod1 <- X*x
prod1

downtime <-c(0,1,2,12,12,14,18,21,21,23,24,25,28,29,30,30,30,33,36,44,45,47,51)
mean(downtime)

median(downtime)

range(downtime)

sd(downtime)

results <- read.table("C:/Users/Samson/Documents/results.txt", header=T)
results$arch1[5] # Print 5th item from arch1 column

attach(results) # Combine to mitigate syntax.
arch1[5] # Print 5th item from arch1 column.

na.rm = T # remove N/A entries
na.rm = TRUE # same as above

mean(arch1, na.rm = T) # get mean from arch1, without N/A entries.
mean(prog1, na.rm = T) # get mean from prog1, without N/A entries.
mean(arch2, na.rm = T) # get mean from arch2, without N/A entries.
mean(prog2, na.rm = T) # get mean from prog2, without N/A entries.

summary(downtime) # self-explanatory
summary(results)

boxplot(downtime)
