# 버블 정렬 : 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘(단순 교환 정렬)
# 액체 속의 공기 방울이 가벼워서 위로 올라오는 모습에서 착안
# 안정적

from typing import MutableSequence
import random
from copy import deepcopy

# 기본 버블 정렬
def bubble_sort(a : MutableSequence) -> None:
    n = len(a)

    cntCompare = 0
    cntChange = 0

    for i in range(n-1):
        exchan = 0
        for j in range(n-1, i, -1):
            cntCompare += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchan += 1
        cntChange += exchan        
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

# 후순위에서 더이상 변경이 없는 경우 그만두는 조건 추가
def bubble_sort_upgrade01(a : MutableSequence) -> None:
    n = len(a)

    cntCompare = 0
    cntChange = 0

    for i in range(n-1):
        exchan = 0
        for j in range(n-1, i, -1):
            cntCompare += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchan += 1
        cntChange += exchan
        # 더이상 변경할 숫자가 없음(개선1)
        if exchan == 0:
            break
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

# 앞 순위도 정렬이 일어나는 부분부터 확인하는 조건 추가
def bubble_sort_upgrade02(a : MutableSequence) -> None:
    n = len(a)

    k = 0

    cntCompare = 0
    cntChange = 0

    # 정렬된 이후 지점부터만 비교
    while k < n-1:
        last = n-1
        exchan = 0
        for j in range(n-1, k, -1):
            cntCompare += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
                exchan += 1
        k = last
        cntChange += exchan
        # 더이상 변경할 숫자가 없음(개선1)
        if exchan == 0:
            break               

    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

# 더 개선된 방법(이동을 작은 쪽 큰쪽 번갈아가면서)
def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right

    cntCompare = 0
    cntChange = 0

    while left < right:
        for j in range(right, left, -1):
            cntCompare += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
                cntChange += 1
        left = last

        for i in range(left, right):
            cntCompare += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
                cntChange += 1

        right = last

    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")


num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])
bubble_sort(deepcopy(x))
bubble_sort_upgrade01(deepcopy(x))
bubble_sort_upgrade02(deepcopy(x))
shaker_sort(deepcopy(x))
print(x[:10])

y = [1, 3, 9, 4, 7, 8, 6]
bubble_sort(deepcopy(y))
bubble_sort_upgrade01(deepcopy(y))
bubble_sort_upgrade02(deepcopy(y))
shaker_sort(deepcopy(y))