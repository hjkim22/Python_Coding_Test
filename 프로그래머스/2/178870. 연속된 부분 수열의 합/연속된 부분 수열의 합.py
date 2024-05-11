def solution(sequence, k):
    start, end = 0, 0
    min_length = float('inf')
    min_indices = []

    current_sum = sequence[start]

    while start < len(sequence):
        if current_sum == k:
            length = end - start + 1
            if length < min_length:
                min_length = length
                min_indices = [start, end]
            elif length == min_length:
                min_indices = [min(min_indices[0], start), min_indices[1]]
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            end += 1
            if end == len(sequence):
                break
            current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1

    return min_indices

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))