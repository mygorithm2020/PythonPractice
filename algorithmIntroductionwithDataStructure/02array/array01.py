list = list(range(7))
print(list)

list2 = [None] * 5
print(list2)
list2[3] = 5
print(list2)

a = list
b = list
print(id(list), id(a), id(b))
list[1] = 10
print(list)
print(a)
print(b)
print(id(list), id(a), id(b))

q = [1, 2, 3]
w = [1, 2, 3]
print(id(q), id(w))
if q == w:
    print("same.....")

e = [2, 2, 5]
r = e.copy()
print(e, r)
print(id(e), id(r))
if e == r:
    print("smsdmsdmsm")
r[1] = 10
print(e, r)

def importTest():
    print("이건 import 된 부분입니다.")
    if __name__ == "__main__":
        print("원본에서 사용한 부분입니다")

importTest()