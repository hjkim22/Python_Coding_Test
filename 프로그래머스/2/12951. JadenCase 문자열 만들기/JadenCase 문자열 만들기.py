def solution(s):
    answer = ''
    capitalize_next = True
    
    for char in s:
        if capitalize_next:
            answer += char.upper()
            capitalize_next = False
        else:
            answer += char.lower()
        
        if char == ' ':
            capitalize_next = True
    
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))