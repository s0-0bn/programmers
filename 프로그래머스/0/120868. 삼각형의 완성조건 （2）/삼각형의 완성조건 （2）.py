def solution(sides):
    answer = 0
    long = max(sides)
    short = min(sides)
    
    for _ in range(long-short,long):
        answer+=1
    
    for _ in range(long+1, short+long):
        answer+=1    
    
    return answer