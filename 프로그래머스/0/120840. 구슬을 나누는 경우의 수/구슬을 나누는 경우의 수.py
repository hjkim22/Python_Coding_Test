import math

def solution(balls, share):
    result = math.comb(balls, share)
    return result

print(solution(3, 2))
print(solution(5, 3))