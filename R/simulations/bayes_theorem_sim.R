h <- .15
not_h <- 1 - h
p_h <- .95
p_not_h <- .02

# Looking for:
# p(h|p), p(-h|p), p(h|-p), p(-h|-p)

p <- h * p_h + not_h * p_not_h
h_p <- h * p_h / p
not_h_p <- not_h * p_not_h / p
not_p <- 1 - p
not_p_h <- 1 - p_h
h_not_p <- h * not_p_h / not_p
not_h_not_p <- 1 - h_not_p

# =================================
# Without Simulation is above.
# With Simulation is below:
# =================================

pos <- 0
virus <- 0

for (i in c(1:10000)){
  if (runif(1) < .15) {
    virus[i] <- 1
    if (runif(1) < .95) {
      pos[i] <- 1
    } else {
      pos[i] <- 0
    }
  } else {
    virus[i] <- 0
    if (runif(1) < .1595) {
      pos[i] <- 1
    } else {
      pos[i] <- 0
    }
  }

}

sum(pos) / 10000

sum(pos & virus) / sum(pos)

sum(!pos & virus) / sum(!pos)
