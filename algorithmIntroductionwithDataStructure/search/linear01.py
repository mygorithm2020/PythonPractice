from typing import Any, Sequence
import copy
def seq_search(a: Sequence, key: Any) -> int:
    ans = -1
    for i in range(len(a)):
        if a[i] == key:
            ans = i
            break
    
    return ans

# 보초법을 적용한 예제(구하고자 하는 값을 맨 끝에 넣어서 무조건 값을 존재하게 만들기)
def seq_search02(a: Sequence, key : Any) -> int:
    ans = -1
    ca = list(copy.deepcopy(a))
    ca.append(key)
    i = 0
    while(True):
        if ca[i] == key:
            ans = i
            break
        i+=1
    
    print(ans, len(ca))
    ans = -1 if ans == len(ca)-1 else ans
    return ans

if __name__ == "__main__":
    num = 10
    x = [None] * num
    
    for i in range(num):
        x[i] = i
    
    ky = 11
    idx = seq_search(x, ky)
    if idx == -1:
        print("no key")
    else:
        print(f"find key is {idx}")

    idx = seq_search02(x, ky)

    if idx == -1:
        print("no key")
    else:
        print(f"find key is {idx}")
    
    temp = "sadassdx"
    qqq = seq_search02(temp, "q")
    print(qqq)