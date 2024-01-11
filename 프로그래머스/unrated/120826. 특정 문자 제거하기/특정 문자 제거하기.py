def solution(my_string, letter):
    answer = ''.join(char for char in my_string if char != letter)
    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))