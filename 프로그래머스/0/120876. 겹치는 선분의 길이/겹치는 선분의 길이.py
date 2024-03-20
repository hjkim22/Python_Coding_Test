def solution(lines):
    points = []
    for line in lines:
        points.extend(line)
    points.sort()

    overlap_length = 0
    
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        count = 0
        for line in lines:
            if start >= line[0] and end <= line[1]:
                count += 1
        if count >= 2:
            overlap_length += end - start

    return overlap_length

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))