import math
n = int(input())
m = int(input())
k = int(input())
w = m*n

if ((k%n == 0) or (k%m == 0)) and (w >= k):
    print("YES")
else:
    print("NO")