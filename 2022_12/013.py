if __name__ == '__main__':
    n = int(input())
    custom_queue = [(i+1) for i in range(n)]

    answer = -1
    while custom_queue:
        answer = custom_queue.pop(0)
        
        if custom_queue:
            custom_queue.append(custom_queue.pop(0))
        
    print(answer)