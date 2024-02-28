# KMP (Knuth-Morris-Pratt) 법 : 사람이름에서 따온것, 앞선 검사 결과를 효율적으로 사용가능한 알고리즘
# 텍스트 길이 = n, 패턴의 길이 = m => 시간 복잡도 O(n)

def kmp_match(txt:str, pat:str) -> int:
    pt = 1   # txt 커서
    pp = 0      # pat 커서
    skip = [0] * (len(pat) + 1)

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt +=1
            pp +=1
            skip[pt] == pp
        elif pp == 0:
            pt +=1
            skip[pt] = pp
        else:
            pp = skip[pp]
        
    
    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp ==0:
            pt +=1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1



s1 = "testyoungstring"
s2 = "oun"

idx = kmp_match(s1, s2)
if idx == -1:
    print("no matched text in string")
else:
    print(idx, " matched loc")