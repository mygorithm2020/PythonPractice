# 브루트 포스법 (brute force method) : 선형 검색을 단순하게 확장한 알고리즘, 단순법
# 이미 검사한 위치를 기억하지 못하므로 효율이 좋지 않음
# # 텍스트 길이 = n, 패턴의 길이 = m => 시간 복잡도 O(nm), 실제로는 o(n)

def bf_match(txt: str, pat: str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt +=1
            pp +=1
        else:
            pt = pt - pp + 1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1

s1 = "testyoungstring"
s2 = "oun"

idx = bf_match(s1, s2)
if idx == -1:
    print("no matched text in string")
else:
    print(idx, " matched loc")