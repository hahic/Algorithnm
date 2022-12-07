if __name__ == '__main__':
    n = int(input())
    a = [0 for i in range(n)]
    
    for i in range(n):
        a[i] = int(input())
        
    stack = []
    number = 1
    result = True
    answer = ""
    
    for i in range(n):
        su = a[i]
        
        if su >= number:
            while su >= number:
                stack.append(number)
                number += 1
                answer += '+\n'
            
            stack.pop()
            answer += '-\n'
        else:
            n = stack.pop()
            
            if n > su:
                print('NO')
                result = False
                break
            else:
                answer += '-\n'
                
    if answer:
        print(answer)
        