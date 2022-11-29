import time
import asyncio


async def print_async(data: int) -> None:
    await asyncio.sleep(1)
    print("(func) print_sync -> " + str(data))
    
async def main():
    await asyncio.gather(
        print_async(1),
        print_async(2),
        print_async(3),
        print_async(4),
        print_async(5)
    )


if __name__ == '__main__':
    start = time.time()
    print("start time: " + str(start))
   
    asyncio.run(main())   # 시작
    
    end = time.time()
    print("end time: " + str(end))
    print("elapsed time: " + str(end-start))