from itertools import permutations
def solution(spell, dic):
    box = []
    for perm in permutations(spell,len(spell)):
        if ''.join(perm) in dic:
            return 1
    return 2


def solution2(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2