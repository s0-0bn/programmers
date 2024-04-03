#... .count가 된다....
# bin_check를 만들 필요가 없었다
# bin(n)[2:].count('1')
def bin_check(n):
    bin_n = bin(n)[2:]
    cnt=0
    
    for i in bin_n:
        if i=='1':
            cnt+=1
    return cnt


def solution(n):
    print(bin(n).count('1'))
    ans = bin_check(n)
    while True:
        box = bin_check(n+1)
        if ans == box:
            return n+1
        n+=1
    return n+1