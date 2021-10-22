# 二分探査における解説
## 目的
- 単純な自己満です、記録に残したいというただそれだけです。
## 疑問点
```
def search(data,num):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right)//2
        if data[mid] == num:
            return "yes"
        elif data[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return "no"
```
- right  = len(date) -1 となる理由
    - 配列に番号を振ればすぐにわかる。配列は0から数えられるのに対し、配列の数は1から数えられるためその調整を行なっている。
```
list_num = [1,2,3,4,5]
print(len(list_num))
>>> 5
```
- left = mid + 1, right = mid - 1 の "-1"
    - midがそもそもif data[mid] == num:　で違うとがわかっているため、midを除いたところを端にすればいいことになる。