n = int(input())
arr = list(map(int, input().split()))

positive_cnt = len([x for x in  arr if x >= 0])

print(positive_cnt)