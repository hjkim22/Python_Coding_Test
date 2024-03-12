def solution(N, stages):
    failure_rate = {}
    total_players = len(stages)
    
    for stage in range(1, N + 1):
        if total_players == 0:
            failure_rate[stage] = 0
        else:
            players_on_stage = stages.count(stage)
            failure_rate[stage] = players_on_stage / total_players
            total_players -= players_on_stage
    
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))