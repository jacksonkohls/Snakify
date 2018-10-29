a = int(input())
b = int(input())
c = int(input())
x = 0
y = 0

if a > c:
    x = x + 1
if b > c:
    x = x + 1
if a > b:
    y = y + 1

if x == 0:
    if y == 0:
        print (a)
    else:
        print (b)
elif x == 2:
    print (c)
   