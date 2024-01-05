def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

num1_1, num1_2 = 2, 11
num2_1, num2_2 = 3, 11
num1_3, num2_3 = 7, 99

print(solution(num1_1, num2_1))
print(solution(num1_2, num2_2))
print(solution(num1_3, num2_3))