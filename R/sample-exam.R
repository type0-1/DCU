chickwts

attach(chickwts)

# Q1.A 

boxplot(weight~feed)

# Q1.B  

tapply(weight, feed, mean) # Mean
tapply(weight, feed, var) # Variance

#Q1.C 

linseed <- sum(chickwts$weight < 159 & chickwts$feed == "linseed")
sunflower <- sum(chickwts$weight < 159 & chickwts$feed == "sunflower")

((linseed + sunflower) - (linseed * sunflower)) / sum(chickwts$weight < 159)

# Q2 

no_of_defectives <- 0
iterations <- 10000

for(i in c(1:iterations)){
  j <- 1
  while(TRUE){
    if(runif(1) <= .2){
      no_of_defectives[i] <- j
      break
    }
    j <- j + 1
  }
}

length(no_of_defectives[no_of_defectives == 5]) / iterations

