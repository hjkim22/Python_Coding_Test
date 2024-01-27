def solution(order):
    count = 0
    for digit in str(order):
        if digit in ['3', '6', '9']:
            count += 1
    return count

print(solution(3))
print(solution(29423))