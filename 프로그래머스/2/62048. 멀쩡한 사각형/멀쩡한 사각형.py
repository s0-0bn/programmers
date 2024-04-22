def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

def solution(w, h):
    whole = w * h;
    broken = w + h - gcd(w, h)
    return whole - broken