n = int(input())
res1 = 1
res2 = 0
for i in range(1, n+1):
    res1*=i
    res2+= res1
print(res2)