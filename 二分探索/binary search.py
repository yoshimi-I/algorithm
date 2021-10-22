# 二分探査に関するアルゴリズム
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
list_num = [1,2,3,4,5]
print(len(list_num))