def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        ans = 0
        for j in name:
            if j in i:
                ans+=yearning[name.index(j)]
        answer.append(ans)
    return answer