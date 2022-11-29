import time


def print_sync(data: int) -> None:
    time.sleep(1)
    print("(func) print_sync -> " + str(data))
    
def main():
    print_sync(1)
    print_sync(2)
    print_sync(3)
    print_sync(4)
    print_sync(5)
    

if __name__ == '__main__':
    start = time.time()
    print("start time: " + str(start))
   
    main()   # 시작
    
    end = time.time()
    print("end time: " + str(end))
    print("elapsed time: " + str(end-start))
    
    
    