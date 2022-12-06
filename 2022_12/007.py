if __name__ == '__main__':
    n = int(input())
    m = int(input())
    answer = 0
    
    custom_list = list(map(int, input().split()))
    custom_list.sort()
    
    start_index = 0
    end_index = len(custom_list) - 1
    
    while start_index < end_index:
        start_value = custom_list[start_index]
        end_value = custom_list[end_index]
        
        if (start_value + end_value) < m:
            start_index += 1
        elif (start_value + end_value) > m:
            end_index -= 1
        else:
            start_index += 1
            end_index -= 1
            
            answer += 1
            
    print(answer)
    