# 단순 삽입 정렬 (insertion sort) : 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬하는 알고리즘입니다. 
# 단순 선택 정렬과 비슷해 보이지만 값이 가장 작은 원소를 선택하지 않는다는 점이 다릅니다.
# 원소를 순차적으로 골라 정렬된 부분에 넣고 뒤로 미는느낌
# 장점 : 이미 정렬을 마쳤거나 정렬이 거의 끝나가는 상태에서는 속도가 아주 빠르다
# 단점 : 삽입할 위치가 멀리 떨어져 있으면 이동 횟수가 많아집니다.
# 안정적

from copy import deepcopy
import random
from typing import MutableSequence
import bisect

def insertion_sort(a : MutableSequence) -> None:
    n = len(a)

    cntCompare = 0
    cntChange = 0

    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            cntCompare += 1
            cntChange += 1
            a[j] = a[j-1]
            j -= 1    
        cntChange += 1    
        a[j] = tmp
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")


# 이진 삽입정렬로 개선
def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)

    cntCompare = 0
    cntChange = 0

    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1        

        while True:
            cntCompare += 1
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1                
            elif a[pc] > key:
                pr = pc - 1
            
            if pl > pr :
                break
        
        cntCompare += 1
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            cntChange += 1
            a[j] = a[j-1]
        cntChange += 1
        a[pd] = key
    
    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

# 파이썬 이진 삽입 정렬 알고리즘 사용

def binary_insertion_sort_upgrade01(a : MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
    

num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])
x2 = deepcopy(x)
insertion_sort(x2)
print(x2[:10])

x3 = deepcopy(x)
binary_insertion_sort(x3)
print(x3[:10])

x4 = deepcopy(x)
binary_insertion_sort(x4)
print(x4[:10])