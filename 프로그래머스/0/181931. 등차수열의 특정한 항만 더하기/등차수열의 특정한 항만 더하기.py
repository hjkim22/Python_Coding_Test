def solution(a, d, included):
    n = len(included)
    total = 0
    current_term = a
    
    for i in range(n):
        if included[i]:
            total += current_term
        current_term += d
    
    return total

print(solution(3, 4, [True, False, False, True, True]))
print(solution(7, 1, [False, False, False, True, False, False, False]))