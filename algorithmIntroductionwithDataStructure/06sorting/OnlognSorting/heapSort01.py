# 힙 정렬(heap sort) : 선택 정렬을 응용한 알고리즘, 힙의 특성을 이용하여 정렬하는 알고리즘
# 힙은 '부모의 값이 자식의 값보다 항상 크다'는 조건을 만족하는 완전 이진 트리입니다. 혹은 그 반대도 가능
# 즉, 두 값의 대소 관계가 일정하면 됨

from copy import deepcopy
import random
from typing import MutableSequence

def heap_sort(a : MutableSequence) -> None:
    def down_heap(a: MutableSequence, left:int, right:int) ->None:
        temp = a[left] #루트

        parent = left
        while parent < (right+1)// 2:
            cl = parent * 2 + 1 #왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <=right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child

        a[parent] = temp
    
    n = len(a)

    for i in range((n-1)//2, -1, -1):
        down_heap(a, i, n-1)
    
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)


num = 10
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
heap_sort(x1)
print(x1[:10])