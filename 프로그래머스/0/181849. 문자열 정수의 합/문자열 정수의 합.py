def solution(num_str):
    total = 0
    
    for digit in num_str:
        total += int(digit)
    
    return total

print(solution("123456789"))
print(solution("1000000"))