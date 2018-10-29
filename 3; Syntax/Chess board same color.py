x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

p1 = x1 + y1
p1 = p1%2
p2 = x2 + y2 
p2 = p2%2
if (p1 == p2):
    print("YES")
else:
    print("NO")