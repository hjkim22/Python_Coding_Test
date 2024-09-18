def solution(progresses, speeds):
    answer = []
    dates = []
    count = 0
    
    for p, s in zip(progresses, speeds):
        date = -((p-100) // s)
        dates.append(date)
    
    dates.append(float("inf"))
    cnt_date = dates[0]
    for date in dates:
        if date <= cnt_date:
            count += 1
        else:
            answer.append(count)
            cnt_date = date
            count = 1
    
    return answer