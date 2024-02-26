def solution(my_string):
    counts = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            counts[index] += 1
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
            counts[index] += 1
    
    return counts

my_string = "Programmers"

print(solution(my_string))
