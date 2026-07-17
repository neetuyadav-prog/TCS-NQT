n = int(input())
arr = list(map(int,input().split()))

min_num = arr[0]
for i in arr:
  if i < min_num:
    min_num = i
print(min_num)
