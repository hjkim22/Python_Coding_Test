def is_valid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1
    
    return answer

s1 = "[](){}"
s2 = "}][[{"
s3 = "[)(]"
s4 = "}}}"
print(solution(s1)) 
print(solution(s2)) 
print(solution(s3))
print(solution(s4))