def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    return max(num1, num2)

print(solution(9, 91))
print(solution(89, 8))