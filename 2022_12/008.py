if __name__ == '__main__':
    n = int(input())
    answer = 0
    
    custom_list = list(map(int, input().split()))
    custom_list.sort()
    
    start_index = 0
    end_index = len(custom_list) - 1
    target_index = 0
    
    while target_index != len(custom_list):
        target_value = custom_list[target_index]
        
        while start_index < end_index:
            start_value = custom_list[start_index]
            end_value = custom_list[end_index]
            
            if (start_value + end_value) == target_value:
                answer += 1
                break
            elif (start_value + end_value) < target_value:
                start_index += 1
            else:
                end_index -= 1
            
        start_index = 0
        end_index = len(custom_list) - 1
        target_index += 1
        
    print(answer)