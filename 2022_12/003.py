if __name__ == '__main__':
    n, question = map(int, input().split())
    custom_list = list(map(int, input().split()))
    custom_sum_list = [0]
    
    sum = 0
    for i in custom_list:
        sum = sum + i
        custom_sum_list.append(sum)
        
    for i in range(question):
        a, b = map(int, input().split())
        print(custom_sum_list[b] - custom_sum_list[a-1])
