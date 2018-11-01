n = int(input())
p=0
for i in range(n-1):
    x = int(input())
    p+=x
o = (n*(n+1))//2 - p
print(o)