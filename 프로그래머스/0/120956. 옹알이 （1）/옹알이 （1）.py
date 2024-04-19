def solution(babbling):
    answer = 0
    box = []
    babe = ['aya','ye','woo','ma']
    
    for i in babbling:
        for j in babe:
            if j in i:
                i = i.replace(j,'%%')
        box.append(i)
    for i in box:
        if set(i) == {"%"}:
            answer+=1
    return answer