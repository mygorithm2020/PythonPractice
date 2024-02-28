# 셸 정렬 (shell sort) : 단순 삽입 정렬의 장점은 살리고 단점은 보완하여 더 빠르게 정렬하는 알고리즘 입니다.
# 먼저 정렬할 배열의 원소를 그룹으로 나눠 각 그룹별로 정렬(삽입정렬)을 수행. 그 후 정렬된 그룹을 합치는 작업을 반복하여 원소의 이동 횟수를 줄이는 방법



from copy import deepcopy
import random
from typing import MutableSequence

def shell_sort(a : MutableSequence) -> None:
    n = len(a)
    h = n // 2
    cntCompare = 0
    cntChange = 0

    while h > 0 :
        # 전체를 h 등분 해서 비교
        # i는 h 등분의 뒤쪽 값을 의미함
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            # 앞쪽 숫자가 기준 값보다 더 크면(삽입정렬 과정)
            while j >= 0 and a[j] > tmp:
                cntCompare += 1
                cntChange += 1
                a[j+h] = a[j]
                j -= h
            cntChange += 1
            a[j+h] = tmp
        h //= 2
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

# 개선 버전 h값을 더 효율적으로 설정(기존에는 h 값이 서로가 배우가 되어서 효율이 낮음....=> 이해 못함..)
def shell_sort_up01(a : MutableSequence) -> None:    
    cntCompare = 0
    cntChange = 0

    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0 :
        # 전체를 h 등분 해서 비교
        # i는 h 등분의 뒤쪽 값을 의미함
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            # 앞쪽 숫자가 기준 값보다 더 크면(삽입정렬 과정)
            while j >= 0 and a[j] > tmp:
                cntCompare += 1
                cntChange += 1
                a[j+h] = a[j]
                j -= h
            cntChange += 1
            a[j+h] = tmp
        h //= 3
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
shell_sort(x1)
print(x1[:10])

x2 = deepcopy(x)
shell_sort_up01(x2)
print(x2[:10])