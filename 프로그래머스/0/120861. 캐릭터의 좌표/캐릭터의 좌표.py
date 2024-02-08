def solution(keyinput, board):
    answer = [0,0]
    
    x= [0,0,-1,1]
    y= [1,-1,0,0]
    
    for i in keyinput:
        if i == "up" and answer[1]<board[1]//2:
            answer[0] += x[0]
            answer[1] += y[0]
            
        elif i == "down" and answer[1] > -(board[1]//2):
            answer[0] += x[1]
            answer[1] += y[1]
            
        elif i == "left" and answer[0]>-(board[0]//2):
            answer[0] += x[2]
            answer[1] += y[2]
            
        elif i == "right" and answer[0]<board[0]//2:
            answer[0] += x[3]
            answer[1] += y[3]
    
    return answer