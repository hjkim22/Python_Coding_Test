def solution(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    
    if year1 < year2:
        return 1
    elif year1 > year2:
        return 0
    else:
        if month1 < month2:
            return 1
        elif month1 > month2:
            return 0
        else:
            return 1 if day1 < day2 else 0

print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))