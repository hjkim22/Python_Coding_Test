from itertools import permutations

def solution(spell, dic):
    spell_permutations = set(permutations(spell))
    
    for perm in spell_permutations:
        word = ''.join(perm)
        if word in dic:
            return 1
    
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))