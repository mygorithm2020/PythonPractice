
# 하노이의 탑 : 쌓아놓은 원반을 최소 횟수로 옮기는 알고리즘

# 이해가 안됨.....

def move(no : int, x: int, y : int) -> None:
    if no > 1:
        move(no-1, x, 6-x-y)
    
    if no > 1:
        move(no-1, 6-x-y, y)

move(3, 1, 3)