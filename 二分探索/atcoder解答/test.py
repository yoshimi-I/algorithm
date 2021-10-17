N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = -1
left = -1
right = N
if A[N-1] >= K:
    while abs(right-left) > 1:
        mid = (left + right)//2
        if A[mid] >= K:
            right = mid
        else:
            left = mid
    ans = right
print(ans)