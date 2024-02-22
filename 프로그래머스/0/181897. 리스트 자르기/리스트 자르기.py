def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]

n1, slicer1, num_list1 = 3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]
n2, slicer2, num_list2 = 4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(solution(n1, slicer1, num_list1))
print(solution(n2, slicer2, num_list2))