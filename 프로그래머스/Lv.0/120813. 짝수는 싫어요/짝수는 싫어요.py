def solution(n):
    odd_num = [i for i in range(1, n+1) if i % 2 != 0]
    return odd_num

print(solution(10))
print(solution(15))