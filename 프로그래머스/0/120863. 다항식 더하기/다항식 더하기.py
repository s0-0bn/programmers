def solution(polynomial):
    answer = 0
    x = [i for i in polynomial.split(' ') if "x" in i ]
    num = [int(i) for i in polynomial.split(' ') if "x" not in i and i!="+" ]   
    
    for i in x:
        if i.split("x")[0]=='':
            answer+=1
        else: 
            answer+=int(i.split("x")[0])
    
    if len(x)==0:
        return str(eval(polynomial))
    
    elif sum(num)==0:
        if answer == 1:
            return "x"
        return str(answer)+"x" 
    
    elif answer==1:
        return "x"+" + "+str(sum(num))
    
    
    return str(answer)+"x"+" + "+str(sum(num))