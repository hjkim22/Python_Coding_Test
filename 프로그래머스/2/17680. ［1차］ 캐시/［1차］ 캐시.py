def solution(cacheSize, cities):
    from collections import deque
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque(maxlen=cacheSize)
    cache_set = set()
    time = 0
    
    for city in cities:
        city = city.lower()
        if city in cache_set:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) >= cacheSize:
                removed_city = cache.popleft()
                cache_set.remove(removed_city)
            cache.append(city)
            cache_set.add(city)
            time += 5
    
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))