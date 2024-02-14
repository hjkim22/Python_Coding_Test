def solution(my_string, is_suffix):
    suffix_length = len(is_suffix)
    if my_string[-suffix_length:] == is_suffix:
        return 1
    else:
        return 0

print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))