def solution(k, score):
    answer = []
    final = []
    for i in score:
        if len(answer)<k:
            answer.append(i)
        elif len(answer)>=k:
            if i>=min(answer):
                answer.pop(0)
                answer.append(i)
        answer.sort()
        final.append(min(answer))
    return final