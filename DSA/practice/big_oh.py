"""
Algorithm Analysis Notes

Purpose of Algorithm Analysis:

Algorithm analysis aims to determine the time complexity of a function, denoted as f(n), and relate it to a specific time complexity represented as g(n).

============================================

Different Time Complexities:

O(1): Constant time.
O(log(n)): Logarithmic time.
O(sqrt(n)): Square Root time.
O(n): Linear time.
O(nlog(n)): Logarithmic times n.
O(n * m): Quadratic time, where n != m.
O(n^2): Quadratic time, where n = m (a special case of O(n * m)).

============================================

Asymptotic Notation:

O (Big-Oh): Worst-case.
Ω (Big-Omega): Average-case.
Θ (Big-Theta): Best-case.

============================================

Proofs in Algorithm Analysis (Big-Oh):

Let:

f(n) -> Algorithm run-time.
g(n) -> Arbitrary time complexity.
c -> A constant, where c > 0.
n0 -> An integer constant, where for every n, n >= n0.
We say that f(n) = O(g(n)) if there exists a constant "c" (c > 0) and an integer constant n0 such that:

f(n) <= c * g(n), for every integer n >= n0.

============================================

Example:

Given:

f(n) = 8n + 5
g(n) = n
Is f(n) = O(g(n)), or is 8n + 5 = O(n)?

============================================

Definition of O(n):

f(n) <= c * g(n), for every integer n >= n0.

Let's solve the inequality:

8n + 5 <= c * n

============================================

For n0, let c = 13 and n = 1:

n0 = (13 * 1 - 5) / 8 = (13 - 5) / 8 = 8 / 8 = 1.
c * g(n) = 13 * 1 = 13
f(n) = 8 * 1 + 5 = 13.

For n1, let c = 14 and n = 1:

n1 = (14 * 1 - 5) / 8 = (14 - 5) / 9 = 8 / 8 = 1.125
c * g(n) = 14 * 1 = 14
f(n) = 8 * 1 + 5 = 13.

For n2, let c = 13 and n = 2:

n2 = (13 * 2 - 5) / 8 = (26 - 5) / 8 = (21 / 8) = 2.625.
c * g(n) = 13 * 2 = 26
f(n) = 8 * 2 + 5 = 21

For every n where n >= n0, every input n in c * g(n) will be greater than or equal to f(n): f(n) <= c * g(n).
"""