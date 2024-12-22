import sys; sys.setrecursionlimit(1000000)

cache = {1:1, 2:2}

def solve(n):
    if n in cache:
        return cache[n]
    
    v = solve(n-1) + solve(n-2)
    cache[n] = v % 1000000007
    return cache[n]

def solution(n):
    return solve(n)