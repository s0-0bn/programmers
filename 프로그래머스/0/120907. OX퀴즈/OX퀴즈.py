def solution(quiz):
    answer = []
    for i in quiz:
        lst = i.split(" ")
        if eval(''.join(lst[0:3])) == int(lst[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

