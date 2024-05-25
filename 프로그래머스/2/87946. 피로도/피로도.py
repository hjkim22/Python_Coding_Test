import itertools

def solution(k, dungeons):
    max_count = 0
    
    for perm in itertools.permutations(dungeons):
        current_fatigue = k
        count = 0
        for minimum, consumption in perm:
            if current_fatigue >= minimum:
                current_fatigue -= consumption
                count += 1
            else:
                break
        max_count = max(max_count, count)
    
    return max_count
