def solution(arr, delete_list):
    for num in delete_list:
        if num in arr:
            arr.remove(num)
    return arr

print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))