def solution(s, n):
    result = ''
    for char in s:
        if char == ' ':
            result += ' '
            continue

        if char.isupper():
            shifted = ord(char) + n
            if shifted > ord('Z'):
                shifted -= 26
            result += chr(shifted)

        elif char.islower():
            shifted = ord(char) + n
            if shifted > ord('z'):
                shifted -= 26
            result += chr(shifted)
    return result

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))