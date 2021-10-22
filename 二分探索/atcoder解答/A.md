# 二分探索の練習問題
## 問題文
- 長さN の整数列 A 
0
​
 ,…,A 
N−1
​
  が与えられます。この数列は小さい値から順番に並ぶようにソートされています。

- また、整数 K が与えられます。A 
i
​
 ≥K であるようなインデックス i のうち、最小のものを出力してください。ただし、そのような i が存在しない場合は -1 を出力してください。
## 制約
- 1≤N≤10^5
- 1≤K≤10^9
- 1≤A0≤⋯≤AN−1≤109
- 入力はすべて整数である。

## 解答
```
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
```