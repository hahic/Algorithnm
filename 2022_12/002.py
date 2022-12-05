if __name__ == '__main__':
    n = input()
    custom_list = list(map(int, input().split()))
    
    custom_max = max(custom_list)
    custom_sum = sum(custom_list)
    answer = custom_sum / custom_max * 100 / int(n)
    
    print(answer)