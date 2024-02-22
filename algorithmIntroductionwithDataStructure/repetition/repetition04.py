import random

while(True):
    try:
        n = int(input("난수의 개수를 입력하세요 : "))
        break
    except:
        print("숫자를 입력해주세요")
        pass


for i in range(n):
    r = random.randint(1, 15)

    if r == 8:
        continue

    print(r, end=" ")

    if r == 15:
        print("\n break for loop")
        break
else:
    print(f"\n create {n}th random digits")


print(f"{1234:2}")
