# K번째 수
# url: https://www.acmicpc.net/problem/1300


import sys


def smaller_count(n: int, x: int) -> int:
    result = 0
    
    for i in range(n):
        row = i + 1
        temp = ((x - 1) // row)
        
        result += n if n < temp else temp
    
    return result


def bigger_count(n: int, x: int) -> int:
    result = 0
    
    for i in range(n):
        row = i + 1
        temp = x // row
        
        result += 0 if n < temp else (n - temp)
    
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    
    min, max, answer = 1, n*n, -1
    while min <= max:
        target = (min + max) // 2
        
        target_s = smaller_count(n, target)
        target_b = bigger_count(n, target)
        
        if target_s >= k:
            max = target - 1
        elif target_b > n*n - k:
            min = target + 1
        else:
            answer = target
            break
    print(answer)