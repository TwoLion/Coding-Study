# 이진탐색 소스코드 : 재귀적 구현


def binary_search(array, target, start, end):
    if start >end:
        return(None)
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    else:
        return binary_search(array, target, mid+1, end)


# 반복문

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return(mid)
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)



if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)


# 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))