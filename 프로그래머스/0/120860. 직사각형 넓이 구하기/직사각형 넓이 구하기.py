def solution(dots): 
    dots.sort()
    ans = abs(dots[0][0]-dots[-1][0])*abs(dots[0][1]-dots[-1][1])
    return ans