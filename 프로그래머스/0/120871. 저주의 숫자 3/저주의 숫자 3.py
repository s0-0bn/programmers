def solution(n):
    box=[]
    for i in range(1, 300):
        if str(i).count("3")==0:
            box.append(i)
    answer = [j for j in box if j%3!=0]    
    return answer[n-1]