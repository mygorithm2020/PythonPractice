# 힙 정렬(heap sort) : 선택 정렬을 응용한 알고리즘, 힙의 특성을 이용하여 정렬하는 알고리즘
# 힙은 '부모의 값이 자식의 값보다 항상 크다'는 조건을 만족하는 완전 이진 트리입니다. 혹은 그 반대도 가능
# 즉, 두 값의 대소 관계가 일정하면 됨

from copy import deepcopy
import random
from typing import MutableSequence
import heapq

def heap_sort(a : MutableSequence) -> None:

    heap = []

    for i in a:
        heapq.heappush(heap, i)
    for j in range(len(a)):
        a[j] = heapq.heappop(heap)

num = 10
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
heap_sort(x1)
print(x1[:10])