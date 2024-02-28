
# 펙토리얼
def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n-1)       # 직접 재귀
    else:
        return 1

n = 5
print(factorial(5))


