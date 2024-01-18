from itertools import permutations
def solution(spell, dic):
    box = []
    for perm in permutations(spell,len(spell)):
        box.append(perm)

    for j in box:
        if ''.join(j) in dic:
            return 1
    return 2