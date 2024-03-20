def solution1(s):
    answer = 0
    cnt = 0

    while s!="1":
        change = ''
        for i in s:
            if i == '0':
                answer+=1
            else:
                change+=i
        s = bin(len(change))[2:]
        cnt+=1
    return [cnt, answer]


def solution(s):
    iteration, cnt = 0,0
    while s != '1':
        iteration +=1
        cnt+=s.count('0')
        s = bin(len(s)-s.count('0'))[2:]
    return [iteration, cnt]