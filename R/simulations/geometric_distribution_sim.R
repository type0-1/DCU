n_iterations <- 10000

first_nth_defective <- 0

for (i in c(1:n_iterations)) {
  j <- 1
  while (TRUE) {
    if (runif(1) < .2) {
      first_nth_defective[i] <- j
      break
    }
    j <- j + 1
  }
}

length(first_nth_defective[first_nth_defective == 5]) / n_iterations

hist(first_nth_defective, prob = TRUE, breaks = 0:50,
     xlab = "Inspection no #", ylab = "Probability of first defective")