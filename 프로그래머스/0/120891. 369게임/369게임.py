import re
def solution(order):
    answer = re.findall(r'[3,6,9]', str(order))
    return len(answer)