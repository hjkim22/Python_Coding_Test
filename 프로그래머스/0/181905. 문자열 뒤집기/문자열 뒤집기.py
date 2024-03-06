def solution(my_string, s, e):

    my_string = list(my_string)
    
    sub_string = my_string[s:e+1]
    sub_string.reverse()
    
    my_string[s:e+1] = sub_string
    
    return ''.join(my_string)

print(solution("Progra21Sremm3", 6, 12))
print(solution("Stanley1yelnatS", 4, 10))