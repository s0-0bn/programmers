def solution(num, total):
    answer=[]
    a = int(((2*total/num) -num+1)/2)
    l = int((2*total/num)-a)
    
    return [i for i in range(a,l+1)]