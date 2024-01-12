def solution(my_string):
    gather = "aeiou"
    result = ''.join(char for char in my_string if char not in gather)
    return result

print(solution("bus"))
print(solution("nice to meet you"))