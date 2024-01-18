def solution(price, money, count):
    answer = 0
    for cnt in range(1,count+1):
        answer+=price*cnt
    return max(0,answer-money)