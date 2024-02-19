def solution(score):
    answer=[]
    
    scores = [i+j for i,j in score]
    sort_scores = sorted(scores, reverse=True)
    
    for i in scores:
        answer.append(sort_scores.index(i)+1)
    
    return answer