def solution(hp):
    general_attack = 5
    soldier_attack = 3
    ant_attack = 1

    general_count = hp // general_attack
    hp_remainder = hp % general_attack

    soldier_count = hp_remainder // soldier_attack
    hp_remainder %= soldier_attack

    ant_count = hp_remainder // ant_attack

    total_count = general_count + soldier_count + ant_count

    return total_count

print(solution(23))
print(solution(24))
print(solution(999))
