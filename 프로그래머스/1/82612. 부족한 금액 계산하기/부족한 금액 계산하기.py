def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2
    answer = total_cost - money
    return max(answer, 0)

print(solution(3, 20, 4))