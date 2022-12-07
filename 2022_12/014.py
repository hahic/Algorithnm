from queue import PriorityQueue

if __name__ == '__main__':
    n = int(input())
    custom_queue = PriorityQueue()
    
    answer = []
    for i in range(n):
        request = int(input())
        
        if request != 0:
            custom_queue.put((abs(request), request))
        else:
            if custom_queue.empty():
                answer.append('0')
            else:
                temp = custom_queue.get()
                answer.append(str(temp[1]))
                
    print()
    print('\n'.join(map(str, answer)))