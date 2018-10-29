# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
q = int(input())

x = q
y = q//10
z = q//100

a = x - y*10
b = y - z*10
c = z

t = a + b + c
print (t)