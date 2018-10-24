# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a= int(input())
b= int(input())
c= int(input())

a1 = a//2
a2 = a%2
aa= a2+a1

b1 = b//2
b2 = b%2
bb= b2+b1

c1 = c//2
c2 = c%2
cc= c2+c1

final = aa + bb + cc
print(str(final))