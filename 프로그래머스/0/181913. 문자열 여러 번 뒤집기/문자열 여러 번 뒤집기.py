def solution(my_string, queries):
    for query in queries:
        start, end = query
        my_string = list(my_string)
        sub_string = my_string[start:end+1]
        sub_string.reverse()

        my_string[start:end+1] = sub_string

        my_string = ''.join(my_string)
    return my_string

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))