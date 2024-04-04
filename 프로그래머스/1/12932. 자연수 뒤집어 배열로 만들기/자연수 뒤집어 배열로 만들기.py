def solution(n):
    reversed_str = str(n)[::-1]
    return [int(char) for char in reversed_str]

n = 12345
print(solution(n))
