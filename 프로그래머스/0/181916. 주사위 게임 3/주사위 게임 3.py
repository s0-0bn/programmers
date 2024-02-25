from collections import Counter
def solution(a, b, c, d):
    answer = 0    
    lst = sorted([a,b,c,d])
    counter = Counter(lst)
    
    if len(counter)==1:
        return 1111*a
    
    elif len(counter)==2:
        p = counter.most_common()[0][0]
        q = counter.most_common()[1][0]
        if counter.most_common()[0][1]==3:   
            return (10 * p+q)**2
        else :
            return (p + q)*abs(p-q)
        
    elif len(counter)==3:
        return counter.most_common()[1][0]*counter.most_common()[2][0]
    
    elif len(counter)==4 :
        return lst[0]
    

def solution2(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)
    