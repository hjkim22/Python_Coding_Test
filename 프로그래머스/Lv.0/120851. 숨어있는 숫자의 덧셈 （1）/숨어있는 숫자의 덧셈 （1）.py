def solution(my_string):
    answer = 0
    
    for c in my_string:
        if c.isdecimal():
            answer += int(c)
    
    return answer
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))