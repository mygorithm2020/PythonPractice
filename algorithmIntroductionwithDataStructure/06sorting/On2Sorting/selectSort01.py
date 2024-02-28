# 단순 선택 정렬(selection sort) : 가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복하며 정렬하는 알고리즘..
# 안정적이지 않은 정렬(같은 숫자의 순서가 바뀔 수 있음..)

from copy import deepcopy
import random
from typing import MutableSequence

def select_sort(a : MutableSequence) -> None:
    n = len(a)

    cntCompare = 0
    cntChange = 0

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            cntCompare += 1
            if a[j] < a[min]:
                min = j
        cntChange += 1
        a[i], a[min] = a[min], a[i]

    print(f"비교 횟수 : {cntCompare}, 변경 횟수 : {cntChange}")

num = 100
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])
x2 = deepcopy(x)
select_sort(x2)
print(x2[:10])