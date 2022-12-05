if __name__ == '__main__':
    n, m = map(int, input().split())
    parts_matrix = list(map(int, input().split()))
    
    custom_matrix = [[0 for i in range(n+1)]]
    for i in range(n):
        temp_parts_matrix, sum = [0], 0
        
        for j in range(n):
            if i == 0:
                sum = sum + parts_matrix[j]
                temp_parts_matrix.append(sum)
                continue

            if i > j:
                temp_parts_matrix.append(custom_matrix[j+1][i+1])
            elif i == j:
                temp_parts_matrix.append(custom_matrix[1][i+1]-custom_matrix[1][i])
            else:
                temp_parts_matrix.append(custom_matrix[1][j+1] - custom_matrix[1][i])
                
        custom_matrix.append(temp_parts_matrix)
        
    count = 0
    for i in range(n):
        for j in range(n):
            if (custom_matrix[i+1][j+1] % m) == 0:
                count = count + 1
                
    if count % 2 == 0:
        print(count//2)
    else:
        print((count+1)//2)
        
    