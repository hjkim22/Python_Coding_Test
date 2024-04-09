def solution(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    
    total_sum = sum(range(min_val, max_val + 1))
    
    return total_sum

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))