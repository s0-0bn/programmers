def solution(s):
    stk = []
    if s[0]==")" or s[-1]=="(":
        return False
    
    for i in s:
        if i=="(":
            stk.append("(")
        else: 
            if "(" in stk:
                stk.pop()
            else:
                return False
    if stk:
        return False
    return True