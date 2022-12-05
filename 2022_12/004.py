if __name__ == '__main__':
    n, question = map(int, input().split())
    custom_matrix = [[0 for i in range(n+1)]]
    
    for i in range(n):
        parts_matrix = list(map(int, input().split()))
        
        parts_sum = [0]
        sum = 0
        for j in parts_matrix:
            sum = sum + j
            parts_sum.append(sum)
        
        custom_matrix.append(parts_sum)
        
        
    for i in range(question):
        x1, y1, x2, y2 = map(int, input().split())
        
        sum = 0
        for i in range((x2-x1)+1):
            x = x1 + i 
            sum = sum + (custom_matrix[x][y2] - custom_matrix[x][y1-1])
            
        print(sum)