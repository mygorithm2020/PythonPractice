
def recur(n: int) -> None:
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

def recur02(n: int) -> None:
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)

recur(4)
print("----------------------")
recur02(4)

# 재귀함수를 비재귀적으로 변환
def recur03(n: int) -> None:

    while n > 0:
        recur03(n-1)
        print(n)
        n = n -2
recur03(4)
print("----------------------")


def recur04(n: int) -> None:

    s = list()

    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        if s:
            n = s.pop()
            print(n)
            n = n -2            
            continue
        break

    while n > 0:
        recur03(n-1)
        print(n)
        n = n -2
recur04(4)
print("----------------------")