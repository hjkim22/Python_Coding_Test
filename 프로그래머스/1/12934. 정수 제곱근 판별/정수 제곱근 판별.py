def solution(n):
    if n ** 0.5 == int(n ** 0.5):
        return (int(n ** 0.5) + 1) ** 2
    else:
        return -1

n1 = 121
n2 = 3

print(solution(n1))
print(solution(n2))