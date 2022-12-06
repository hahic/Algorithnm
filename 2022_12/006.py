if __name__ == '__main__':
    n = int(input())
    answer = 1
    
    start_index = 1
    end_index = 1
    sum = 1
    
    while end_index != n:
        if sum == n:
            end_index = end_index + 1
            sum = sum + end_index
            
            answer = answer + 1
        elif sum < n:
            end_index = end_index + 1
            sum = sum + end_index
        else:
            sum = sum - start_index
            start_index = start_index + 1
            
    print(answer)