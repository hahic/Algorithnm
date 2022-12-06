def check_count(data: list) -> list:
    result = [0 for i in range(4)]
    
    result[0] = data.count('A')
    result[1] = data.count('C')
    result[2] = data.count('G')
    result[3] = data.count('T') 
    
    return result


def check_enable(target: list, compared: list) -> bool:
    result = True
    
    for i in range(4):
        if target[i] < compared[i]:
            result = False
            break
        
    return result


if __name__ == '__main__':
    answer = 0

    n, m = map(int, input().split())
    custom_list = str(input())
    check_list = list(map(int, input().split()))
    
    start_range = 0
    end_range = (start_range + m) - 1
    
    while end_range != len(custom_list):
        target_range = custom_list[start_range:end_range+1]
        
        count_list = check_count(target_range)
        is_enable = check_enable(count_list, check_list)
        
        if is_enable:
            answer += 1
        
        start_range += 1
        end_range += 1
        
    print(answer)
            

       
    
    