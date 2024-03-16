import math
def solution(a, b):
    while math.gcd(a,b)!=1:
        value = math.gcd(a,b)
        a = a//value
        b = b//value
    
    while math.gcd(b,2)!=1:
        value = math.gcd(b,2)
        b = b//value
        
    while math.gcd(b,5)!=1:
        value = math.gcd(b,5)
        b = b//value
    
    # b = 15 14 91 
    if b==1:
        return 1
    return 2


'''
1. 두 값의 최소공배수를 구한다
2. 그걸로 계속 나눠서 작게 만든다
3. 최종적인 값에서 b가 2와 5로만 구성되어 있으면 1 아니면 0
'''