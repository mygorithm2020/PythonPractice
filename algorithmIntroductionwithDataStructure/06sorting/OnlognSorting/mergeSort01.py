# 병합 정렬 (merge sort): 배열을 앞부분과 뒷부분의 두 그룹으로 나누어 각각 정렬한 후 병합하는 작업을 반복하는 알고리즘
# 안정적인 정렬

from copy import deepcopy
import copy
import random
from typing import Sequence, MutableSequence

def merge_sroted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    # 정렬을 마친 a와 b 배열을 합해서 c에 저장
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc +=1
    
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1
def merge_sort(a:MutableSequence)-> None:
    def _merge_sort(a:MutableSequence, left:int, right: int) ->None:
        if left < right:
            center = (left+right)//2

            _merge_sort(a, left, center) # 배열 앞부분 병합정렬
            _merge_sort(a, center, right) # 배열 뒷부분 병합정렬

            p = j = 0 
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i<= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j +=1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k +=1
                j +=1

    n = len(a)
    buff = [None] * n  # 작업용 배열 소멸
    _merge_sort(a, 0, n-1)
    del buff # 작업용 배열 소멸

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = [None for _ in range(len(a) + len(b))]

merge_sroted_list(a, b, c)
print(a, b, c)
d = list(sorted(a + b))
print(d)

num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

x1 = copy.deepcopy(x)
print(x1[:10])
merge_sort(x1)
print(x1[:10])

