def solution(m, n, board):
    # 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board
    
    answer = 0
    # 최소 2줄부터 30줄 까지
    
    # 그냥 바로 생각나는대로 해볼게
    # 한 점 기준 너비 확장으로 통해 연결된 부분 다 지우기
    # 더이상 없을 때까지 반복임
    # 순서가 상관있을거라고 생각했는데 턴제임.. 한 턴에 다 치우고 그 다음에 다 한꺼번에 치우는 느낌
    
    board = list(map(list, board))      
    
    temp = [x for x in range(n)]
    
    while(True):        
        # 중복 제거용
        ran = dict()
        for idx in range(n):
            ran[idx] = set()        
        
        # 지울게 있는지 찾기                
        for y in range(m-1):
            for x in range(n-1):                
                temp = board[y][x]          
                # 빈공간 버리기
                if temp == "3":
                    continue
                
                # 후보군                
                if temp == board[y][x+1] and temp == board[y+1][x] and temp == board[y+1][x+1]:
                    # 중복을 어떻게 해결하지... 흠...                                                             
                    # 이어져 있지 않을 수 있구나.......맞다.....
                    ran[x].add(y)
                    ran[x].add(y+1)
                    ran[x+1].add(y)
                    ran[x+1].add(y+1)                    
                                                                    
        print(ran)        
        exist = False
        for dn in ran:
            for dm in ran[dn]:                
                board[dm][dn] = "3"
                answer += 1
                exist = True
        
        for dn in ran:
            for dm in sorted(ran[dn], reverse = True):
                newM = dm-1                
                while(newM > -1):
                    if board[newM][dn] != "3":
                        board[dm][dn] = board[newM][dn]
                        board[newM][dn] = "3"
                        break
                    newM-=1
                
                
            
        
        print(board)
          
        # 더이상 지울게 없음..        
        if not exist:
            break
    
    # 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작
    return answer

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])