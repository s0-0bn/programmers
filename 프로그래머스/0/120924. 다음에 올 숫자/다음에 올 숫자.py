def solution(common):
    if abs(common[-1]-common[-2]) == abs(common[-2]-common[-3]):
        return common[-1]+(common[-1]-common[-2])
    else:
        return common[-1]*(common[-1]/common[-2])