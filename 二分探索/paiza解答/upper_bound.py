n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
q = int(input())
test = list(int(input()) for _ in range(q))
for i in test:
    left = 0
    right = n-1
    
    while left < right:
        mid = (left + right)//2
        if i >= l[mid]:
            left = mid + 1
        else:
            right = mid
    print(n-right)