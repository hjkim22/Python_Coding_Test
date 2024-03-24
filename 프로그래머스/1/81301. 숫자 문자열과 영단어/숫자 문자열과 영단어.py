def solution(s):
    num_to_word = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    answer = ''
    temp = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            temp += char
            if temp in num_to_word:
                answer += num_to_word[temp]
                temp = ''
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))