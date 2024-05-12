def solution(my_strings, parts):
    result = ""
    
    for i, part in enumerate(parts):
        start, end = part
        substring = my_strings[i][start:end+1]
        result += substring
    
    return result

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
print(solution(my_strings, parts))