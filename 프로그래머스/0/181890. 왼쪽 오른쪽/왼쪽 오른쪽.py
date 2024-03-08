def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []

    pivot_index = 0
    for i, char in enumerate(str_list):
        if char == 'l' or char == 'r':
            pivot_index = i
            break

    if str_list[pivot_index] == 'l':
        return str_list[:pivot_index]
    else:
        return str_list[pivot_index + 1:]

str_list1 = ["u", "u", "l", "r"]
str_list2 = ["l"]
print(solution(str_list1))
print(solution(str_list2))