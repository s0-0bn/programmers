def solution2(my_string):
    return eval(my_string)

def solution(my_string):
    box = []
    num = []
    
    for i in my_string.split(" "):
        if i!= "-" and i!="+":
            num.append(int(i))
        else:
            box.append(i)
    ans = num.pop(0)
    
    while len(num)>0:
        sign = box.pop(0)
        if sign == "+":
            ans += num.pop(0)
        else:
            ans -= num.pop(0)
    return ans