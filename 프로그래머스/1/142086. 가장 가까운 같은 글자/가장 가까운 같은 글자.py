def solution(s):
    box = []
    answer = []
    
    for i in range(len(s)):
        if s[i] not in box:
            box.insert(0,s[i])
            answer.append(-1)
        else:
            answer.append(box.index(s[i])+1)
            box.insert(0,s[i])
    return answer