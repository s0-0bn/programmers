def solution(board):
    field = len(board)
    boom = []
    ans = 0
    
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    
    for i in range(field):
        for j in range(field):
            if board[i][j]==1:
                boom.append((i,j))
                
    for x,y in boom:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<field and 0<=ny<field:
                board[nx][ny] = 1
    
    for i in range(field):
        for j in range(field):
            if board[i][j]==0:
                ans+=1
    
    return ans