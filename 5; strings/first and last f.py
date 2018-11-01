s=str(input())
if s.find('f') == (-1):
    print()
elif (s.find("f") == s.rfind('f')) :
     print(s.find("f"))
else:
    print(s.find("f"), s.rfind('f'))