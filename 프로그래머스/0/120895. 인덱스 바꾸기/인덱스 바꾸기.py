def solution(my_string, num1, num2):
    string_list = list(my_string)
    string_list[num1], string_list[num2] = string_list[num2], string_list[num1]
    
    return ''.join(string_list)
result1 = solution("hello", 1, 2)
print(result1)

result2 = solution("I love you", 3, 6)
print(result2)