def solution(food):
    r_ans = ''
    l_ans = ''
    
    for i in range(1,len(food)):
        a = food[i]//2
        if a>=0:
            r_ans = str(i)*a+r_ans
            l_ans = l_ans+str(i)*a

    return l_ans+'0'+r_ans