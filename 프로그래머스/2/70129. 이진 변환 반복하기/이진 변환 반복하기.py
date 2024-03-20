def solution(s):
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