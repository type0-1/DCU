# Question 1:

has = 0.15 # p(h)
pos_has = 0.95 # p(p | h)
pos_not_has = 0.02 # p(p | not h)
not_has <- 1 - has # p(not h)
not_pos_has_v = 1 - pos_has # p(not p | h)
not_pos_not_v = 1 - pos_not_has # p(not p | not h)
pos = (pos_has * has) + (pos_not_has * not_has) # p(p)
not_pos = 1 - pos #p(not p)

### If positive and negative:

#a: has virus -> p(h | p) -> p(h | not p):

#p(h | p):

has_pos = (has * pos_has)/pos
has_pos

#p(h | not p):

has_not_pos = (has * not_pos_has_v)/not_pos
has_not_pos

#b: doesn't have virus -> p(not h | p) -> p(not h | not p)

#p(not h | p)

not_has_pos = (not_has * pos_not_has)/pos
not_has_pos

#p(not h | not p)

not_has_not_pos = (not_has * not_pos_not_v) / not_pos
not_has_not_pos
