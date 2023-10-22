# Question 1:

x <- (factorial(26) / factorial(26-6)) / 26^6
x

# Question 2:

x <- choose(60, 10) / choose(100, 10)
x

# Question 3:

x <- choose(5, 3) / choose(15, 3)
x

# Question 4:

#a:

x <- 10/50
x

#b:

x <- (40/50 * 10/49) + (10/50 * 9/49)
x

#c:

x <- (10/50 * 9/49)
x

#d:

x <- (40/50 * 10/50) + (10/50 * 10/50)
x

# Question 5 (prob wrong):

x <- 1 - choose(365, 365-5) / 365^5
x

# Question 7:

x <- sample(c("H","T"), 1000, replace=TRUE)
table(x)["H"] / 1000

# Question 8:

x <- sample(c(1,2,3,4,5,6), 600, replace=TRUE)
table <- table(x)
even <- (table[2] + table[4] + table[6]) / 600
even

# Question 9:

x <- sample(c("HH","HT","TH","TT"), 100, replace=TRUE)
table = table(x)
table / 100

# Question 10:

x <- sample(c(-2,2), 100, replace=TRUE)

amy <- 0
jane <- 0
count <- 0

for(i in 1:100){
  if(x[i] == 2){
    amy <- amy + 2
    jane <- jane - 2
  }
  else{
    jane <- jane + 2
    amy <- amy - 2
  }
  if(amy > jane){
    count <- count + 1
  }
}

#a:

count

#b:

amy
