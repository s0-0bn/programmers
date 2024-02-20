def solution(chicken):
    answer = 0
    mod = 0
    
    while chicken>=10:
        answer+=chicken//10
        mod = chicken%10
        
        chicken = mod+(chicken//10)
    return answer


# 1999 199   208   20   28   2    10  1
#       9           8        8     
