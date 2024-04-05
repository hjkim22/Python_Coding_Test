def solution(x):
    digits = [int(d) for d in str(x)]
    
    digit_sum = sum(digits)
    
    if x % digit_sum == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))