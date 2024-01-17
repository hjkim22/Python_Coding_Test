def solution(age):
    alphabet = "abcdefghij"
    
    result = ""
    while age > 0:
        remainder = age % 10
        result = alphabet[remainder] + result
        age = age // 10
    
    return result

print(solution(23))
print(solution(51))
print(solution(100))