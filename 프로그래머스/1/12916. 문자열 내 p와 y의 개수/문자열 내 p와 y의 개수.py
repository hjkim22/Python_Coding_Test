def solution(s):
    p_count = 0
    y_count = 0
    
    for char in s:
        if char.lower() == 'p':
            p_count += 1
        elif char.lower() == 'y':
            y_count += 1
    
    return p_count == y_count

print(solution("pPoooyY"))
print(solution("Pyy"))