def solution(sizes):
    for i in sizes:
        i.sort()
    
    mw = sizes[0][0]
    mh = sizes[0][1]
    
    for w,h in sizes[1:]:
        if w > mw:
            mw = w
        if h > mh:
            mh = h
    return mw*mh