def solution(n):
    colatz_sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        colatz_sequence.append(n)
    return colatz_sequence

print(solution(123123))