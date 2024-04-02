def solution(N):
    return sum(int(digit) for digit in str(N))

print(solution(123))
print(solution(987))