probs <- 0
p <- .5
k <- 1

for (i in c(1:30)) {
  probs[i] <- 1 - (1 - p) ^ k
  k <- k + 1
}

diffs <- 0

for (i in c(2:30)) { 
  diffs[i - 1] <- probs[i] - probs[i - 1]
}

plot(diffs, type = "o", xlab = "No of Additional (Parallel) Components", 
     ylab = "Gain in reliability")