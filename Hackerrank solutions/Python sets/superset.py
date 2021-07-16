a = set(input().split())
n = int(input())
c = 0
for i in range(n):
    b = set(input().split())
    if a.issuperset(b):
        c += 1

print('True' if c == n else 'False')