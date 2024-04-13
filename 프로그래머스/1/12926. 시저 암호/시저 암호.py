def solution(s, n):
    answer=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i in alpha:
            answer += alpha[(alpha.index(i)+n)%26] 
        elif i == ' ':
            answer += ' '
        else:
            answer += alpha[(alpha.index(i.upper())+n)%26].lower()
    return answer