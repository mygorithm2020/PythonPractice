# 데이터가 정렬되어있어야 함!
# 선형검색보다 빠름

from typing import Any, Sequence
import random
from datetime import datetime
import time

def bin_search(a: Sequence, key:Any) ->int:
    pl = 0              #왼쪽 인덱스
    pr = len(a) - 1     # 오른쪽 인덱스
    
    
    while(True):
        pc = (pl + pr) // 2         # 중앙 인덱스
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc -1
        
        if pl > pr :
            break
    
    return -1

def tri_search(a: Sequence, key:Any) ->int:
    pl = 0              #왼쪽 인덱스
    pr = len(a) - 1     # 오른쪽 인덱스
    
    while(True):
        pc1 = (2*pl + pr) // 3        # 1 중앙 인덱스
        pc2 = (pl + 2 * pr) // 3    # 2 중앙 인덱스
        if a[pc1] == key:
            return pc1        
        elif a[pc2] == key:
            return pc2
        else:
            if key < a[pc1]:
                pr = pc1 - 1
            elif key < a[pc2]:
                pl = pc1 + 1
                pr = pc2 - 1
            else:
                pl = pc2 + 1
        
        if pl > pr :
            break
    return -1

if __name__ == "__main__":
    num = 1400000
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(1, num)
    
    x.sort()
    ky = random.randint(1, num)

    print(ky)

    start = time.time()
    print(start)
    time.sleep(1)    
    idx = bin_search(x, ky)
    start2 = time.time()
    print(start2 - start)    
    if idx == -1:
        print("no key")
    else:
        print(f"find key is {idx} in list")

    start3 = time.time()
    print(start3)    
    idx = tri_search(x, ky)
    start4 = time.time()
    print(start4 - start3)    
    if idx == -1:
        print("no key")
    else:
        print(f"find key is {idx} in list")

    print(start, start2, start3, start4)
    print(f"이진탐색 = {start2 - start}, 삼진탐색 = {start4 - start3}")
