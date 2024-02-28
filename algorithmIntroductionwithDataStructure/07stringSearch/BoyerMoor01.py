# 보이어-무어법(Boyer-Moor) : KMP보다 더 효율적이며 실제 문자열 검색에서 널리쓰이는 알고리즘
# # 텍스트 길이 = n, 패턴의 길이 = m => 시간 복잡도 O(n), θ(n / m)

def bm_match(txt: str, pat: str) -> int:

    skip = [None] * 256 # 건너뛰기 표

    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    pt = len(pat) - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp
    
    return -1

s1 = "testyoungstring"
s2 = "oun"

idx = bm_match(s1, s2)
if idx == -1:
    print("no matched text in string")
else:
    print(idx, " matched loc")

