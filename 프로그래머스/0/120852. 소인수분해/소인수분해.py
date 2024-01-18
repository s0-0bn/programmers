def solution(n):    
    i = 2
    ans = []
    
    while i<n+1:
        if n%i==0:
            ans.append(i)
            n = n//i
            if i in ans:
                continue
        i+=1
    return sorted(list(set(ans)))