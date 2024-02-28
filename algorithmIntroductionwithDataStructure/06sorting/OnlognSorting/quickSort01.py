# 퀵 정렬 (quick sort) : 가장 빠른 정렬 알고리즘으로 알려져 있으며 널리 사용 됩니다.
# 피벗(기준) 을 정해 나누어 가는 방법 O(nlogn), 다만 피벗이 최소 값이나 최대 값으로 계속해서 선택된다면 On2
# 분할 정복을 통해 구현, 원소수가 적은 경우에는 그다지 빠르지 않음..
# 안정적이지 않음

from copy import deepcopy
import random
from typing import MutableSequence
import  sys, os 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from On2Sorting import insertionSort01


# 피벗을 기준으로 나누는 코드
def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2] # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x : 
            pr -=1
        
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        
    
    if pl > pr + 1:
        print("피벗과 일치", *a[pr + 1 : pl])
        print("피벗 이상인 그룹입니다.", *a[pr + 1 : n])

# 재귀를 활용한 퀵 정렬 구현
def qsort(a: MutableSequence, left: int, right: int, depth: int) -> None:
    depth += 1
    pl = left
    pr = right
    x = a[(left + right) // 2]

    print(f"{depth}, a[{left}] ~ a[{right}] : ", *a[left : right + 1], a[left : right + 1])

    while pl <= pr :
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1
        if pl <= pr :
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        
    if left < pr: 
        qsort(a, left, pr, depth)
    if pl < right:
        qsort(a, pl, right, depth)

# 실제 퀵정렬 함수, 최초 파라미터를 고정하기 위해 함수 내부에서 다시 호출
def quick_sort(a : MutableSequence) -> None:
    qsort(a, 0, len(a)-1, 0)

# 비재귀적 퀵 정렬
def qsort_up02(a: MutableSequence, left : int, right: int) -> None:
    ran = list()
    ran.append((left, right))

    while ran:
        pl, pr = left, right = ran.pop()
        x = a[(left + right) // 2]

        print(f" a[{left}] ~ a[{right}] : ", *a[left : right + 1], a[left : right + 1])

        while pl <= pr:
            while a[pl] < x : pl +=1
            while a[pr] > x : pr -=1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr :
            ran.append((left, pr))
        if pl < right:
            ran.append((pl, right))

def quick_sort02(a : MutableSequence) -> None:
    qsort_up02(a, 0, len(a)-1)



    
# 피벗값은 전체의 중앙값으로 선택하는 것이 가장 효율적임, 하지만 전체의 중앙값을 구하는건 너무 비효율적이므로 원소의 수가 3개이상이면 맨 앞 원소 3개 중 중앙값을 선택
def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """오름차순 정렬 후 중앙 값의 인덱스를 반환"""
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    
    return idx2

#### 원소수가 9 미만이면 단순 삽입정렬
def qsort_up03(a: MutableSequence, left : int, right: int) -> None:
    if right - left < 9:
        insertionSort01.insertion_sort(a)
        return
    pl = left
    pr = right
    m = sort3(a, pl, (pl+pr)// 2, pr)
    x = a[m] # 피벗 값

    a[m], a[pr-1] = a[pr-1], a[m]
    pl += 1
    pr -= 2
    print(f"{x}, a[{left}] ~ a[{right}] : ", *a[left : right + 1], a[left : right + 1])

    while pl <= pr :
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1
        if pl <= pr :
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        
    if left < pr: 
        qsort_up03(a, left, pr)
    if pl < right:
        qsort_up03(a, pl, right)


def quick_sort03(a : MutableSequence) -> None:
    qsort_up03(a, 0, len(a)-1)

num = 10
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
partition(x1)
print(x1[:10])

x2 = deepcopy(x)
quick_sort(x2)
print(x2[:10])

x3 = deepcopy(x)
quick_sort02(x3)
print(x3[:10])

x4 = deepcopy(x)
quick_sort03(x4)
print(x4[:10])