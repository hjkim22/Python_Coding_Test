import math

def solution(progresses, speeds):
    days_remaining = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    deployments = []
    current_deploy_day = days_remaining[0]
    count = 0
    
    for day in days_remaining:
        if day <= current_deploy_day:
            count += 1
        else:
            deployments.append(count)
            current_deploy_day = day
            count = 1
            
    deployments.append(count)
    
    return deployments
