# 유클리드 호제법 (두 정수의 최대 공약수 구하기)

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd (y, x%y)
    

q = gcd(10, 20)
w = gcd(20, 10)
print(q, w)