def self_num():
    ans=list(range(1,10000))
    new_rst=[]
    i=1

    while i <= 10000 :
        rst=[]
        rst.append(i)
        for a in str(i):
            rst.append(int(a))
        new_rst.append(sum(rst))
        i+=1

    for i in ans:
        if i not in new_rst:
            print(i)
            
            
self_num()