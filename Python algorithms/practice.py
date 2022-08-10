s = 'suhas b'
mys = [x.capitalize() for x in s.split()]
for item in mys:
    print(item,end = ' ')
print(s.title())