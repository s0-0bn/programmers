def solution2(numlist, n):
    answer = []
    numlist.sort(reverse=True)
    box = [abs(i-n) for i in numlist]

    while len(box)>0:
        value =box.index(min(box))
        answer.append(numlist[box.index(min(box))])
        box.pop(value)
        numlist.pop(value)

    return answer

def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])