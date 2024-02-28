# 8 x 8 체스판에 퀸이 서로 공격할 수 없게 배치하는 방법 92가지

pos = [0] * 8 #각 열에서 퀸의 위치
flag_a = [False] * 8 # 각 열에 퀸의 배치 유무
flag_b = [False] * 15 # 대각선 방향
flag_c = [False] * 15 # 대각선 방향


def put() -> None:
    for j in range(8):
        for i in range(8):
            print("■" if pos[i] == j else "□", end=" ")
        print()    
    print()

def set(i: int) -> None:
    for j in range(8):
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[i-j+7]) :
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i-j+7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i-j+7] = False

set(0)