def solution(s):
    box = []
    for i in s:
        if len(box)==0:
            box.append(i)
        else:
            if box[-1] == i:
                box.pop()
            else:
                box.append(i)
    if len(box) == 0:
        return 1
    return 0
