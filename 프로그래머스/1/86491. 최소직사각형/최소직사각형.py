def solution(sizes):
    for i in sizes:
        i.sort()
        
    mw, mh = 0,0
    
    for w,h in sizes:
        mw = max(mw,w)
        mh = max(mh,h)
    return mw*mh

def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col