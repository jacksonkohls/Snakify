import math
# 1 hour = 60 minutes
# 1 hour = pi/6 radians
# pi/6 = 60 minutes
# pi/360 = 60 seconds
# pi/21600 = 1 second
# pi radians = 180 degrees
# pi/21600 radians = 1/120 degrees

h = int(input())
m = int(input())
s = int(input())

m = m + h*60
s = s + m*60
s = float(s)
s = s*1/120
print(s)