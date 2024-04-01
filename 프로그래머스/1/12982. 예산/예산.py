def solution(d, budget):
    
    d.sort()
    count = 0
    for i in d:
        if i <= budget:
            count += 1
            budget -= i
    return count
    


# 1 20 22 + 2 4 5 21 23 시간 초과 되는게 많음
from itertools import combinations
def solution2(d, budget):
    answer = 0
    box = []
    for i in range(len(d),0,-1):
        for j in combinations(d,i):
            if sum(j)==budget:
                return i
    return i

# 1 20 22 + 3 4 7 21 23 통과
def solution3(d, budget):
    if sum(d) == budget:
        return len(d)
    
    answer = budget
    d = sorted(d)
    cnt = 0
    while cnt<=len(d):
        for i in range(cnt,len(d)):
            answer-=d[i]
            if answer==0:
                return i-cnt+1
            elif answer<0:
                answer=budget
                break   
            print(answer)
        cnt+=1
    return 0

'''
1 3 5 6 7  /  10


'''