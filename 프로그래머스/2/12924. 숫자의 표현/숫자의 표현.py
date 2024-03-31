def solution(n):
    lst = [i for i in range(1,n+1)]
    i, cnt, answer = 0, 0, 0

    while i<=n:
        a = sum(lst[cnt:i])
        if a < n:
            i+=1
        elif a ==n:
            answer+=1
            cnt+=1
            i = cnt+1
        elif a >n:
            cnt+=1
            i=cnt+1
    return answer
 

'''
7 
1 2 3 4 5 6 7
1+2+3+4
2+3+4
3+4
4+5
5+6
6+7
7
'''
