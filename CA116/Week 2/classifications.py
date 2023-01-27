#!/usr/bin/env python3

mark = int(input())

first = 70 <= mark
second = 50 <= mark and mark < 70
third = 40 <= mark and mark < 50
fail = 40 > mark

fi_string = "first: "
s_string = "second: "
t_string = "third: "
f_string = "fail: "

first = fi_string + str(first)
second = s_string + str(second)
third = t_string + str(third)
fail = f_string + str(fail)

print(first)
print(second)
print(third)
print(fail)
