a = str(input())
b = a[a.find('h') + 1:]
b = b.replace('h', 'H', b.count('h')-1)
print(a[:a.find("h")+1], b, sep="")