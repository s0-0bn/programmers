# 문제 똑바로 읽자^^
# budget을 0으로 만드는 조합을 찾는게 아니라
# budget 내에서 최대로 물품 지원할 수 있는 부서의 수를 찾는 것
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i <= budget:
            answer += 1
            budget -= i
    return answer