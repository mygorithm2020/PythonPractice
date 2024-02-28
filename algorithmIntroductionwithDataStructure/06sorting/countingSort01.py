# 도수 정렬(counting sort) : 원소의 대소 관계를 판단하지 않고 빠르게 정렬하는 알고리즘으로, 분포수 세기(distribution counting) 정렬이라고도 한다.
# 순서가 바뀌지 않는 안정적인 알고리즘

from copy import deepcopy
import random
from typing import MutableSequence

def fsort(a : MutableSequence, max : int) -> None:
    """도수 정렬"""
    n = len(a)
    f = [0] * (max+1) #누적 도수 분포표
    b = [0] * n             # 작업용 임시 배열

    for i in range(n):
        f[a[i]] += 1
    for i in range(1, max + 1):
        f[i] += f[i - 1]        # 누적 숫자 만들기
    
    for i in range(n-1, -1, -1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]       # 임시 배열에 정렬된 위치에 값 넣기
    for i in range(n):
        a[i] = b[i]         # 정렬 결과 원래 배열에 반영
    

def counting_sort(a: MutableSequence) -> None:
    fsort(a, max(a))


num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
counting_sort(x1)
print(x1[:10])

