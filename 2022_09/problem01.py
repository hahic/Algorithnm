# 예산
# URL: https://www.acmicpc.net/problem/2512

import sys, copy


def calculate_needed_budget(data: list, target: int) -> int:
    result = 0
    
    for d in data:
        result += min(d, target)
        
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline().rstrip())
        
    
    min, max = 0, max(data)  
    loop = True
    while(min <= max):
        mid = (min + max) // 2
        
        if calculate_needed_budget(data, mid) <= budget:
            target = mid
            min = mid + 1
        else:
            max = mid - 1
            
    
    answer = -1
    for d in data:
        d_budget = min(d, target)
        answer = max(answer, d_budget)
    print(answer)
                