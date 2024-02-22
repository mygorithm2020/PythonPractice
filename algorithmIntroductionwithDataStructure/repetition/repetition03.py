print("직사각의형의 넓이를 입력하세요")
a = int(input("넓이: "))

for idx in range(1, int(a**0.5) + 1):
    if a%idx:
        continue
    print(f"{idx} x {a//idx} = {a}")

