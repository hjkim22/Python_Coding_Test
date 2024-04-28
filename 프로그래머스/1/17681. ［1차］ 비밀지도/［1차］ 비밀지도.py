def solution(n, arr1, arr2):
    def to_binary(x):
        binary = bin(x)[2:]
        return '0' * (n - len(binary)) + binary
    
    def merge_binary(bin1, bin2):
        result = ""
        for i in range(n):
            if bin1[i] == '1' or bin2[i] == '1':
                result += '#'
            else:
                result += ' '
        return result
    
    decoded_map = [merge_binary(to_binary(arr1[i]), to_binary(arr2[i])) for i in range(n)]
    
    return decoded_map
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
