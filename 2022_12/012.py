if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    custom_stack = []
    answer = [0 for i in range(n)]
    
    for i in range(n):
        while custom_stack and a[custom_stack[-1]] < a[i]:
            answer[custom_stack.pop()] = a[i]
        custom_stack.append(i)
        
    while custom_stack:
        answer[custom_stack.pop()] = -1
        
    result = " ".join(map(str, answer))
    print(result)
    