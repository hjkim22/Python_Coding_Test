def solution(num_list):
    even_number = 0
    odd_number = 0
    for i in num_list:
        if i % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    return even_number, odd_number
    

num1 = [1, 2, 3, 4, 5]
num2 = [1, 3, 5, 7]

print(solution(num1))
print(solution(num2))