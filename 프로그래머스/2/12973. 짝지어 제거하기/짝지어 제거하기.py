def solution(s):
    box = []
    for i in s:
        if box==[]:
            box.append(i)
        else:
            if box[len(box)-1] == i:
                box.pop()
            else:
                box.append(i)
    if box == []:
        return 1
    return 0
