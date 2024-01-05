def solution(money):
    return [money // coffee, money % coffee]

coffee = 5500

print(solution(5500))
print(solution(15000))