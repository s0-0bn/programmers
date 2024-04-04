def solution2(sizes):
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

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col