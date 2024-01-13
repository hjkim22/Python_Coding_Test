def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    result_numer = numer1 * denom2 + numer2 * denom1
    result_denom = denom1 * denom2
    
    greatest_common_divisor = gcd(result_numer, result_denom)
    
    result_numer //= greatest_common_divisor
    result_denom //= greatest_common_divisor
    
    return [result_numer, result_denom]

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))