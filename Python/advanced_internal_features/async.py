import aiohttp
import asyncio
import requests
import multiprocessing as mp
import time
import threading
import queue


def do_requests1():
    return requests.get('https://example.com')


def main1():
    for _ in range(0, 10):
        r = do_requests1()
        print('example.com =>', r.status_code)


def do_requests2(queue, id):
    r = requests.get('https://example.com')
    queue.put((id, r.status_code))


def main2():
    processes = []
    result_queue = mp.Queue()
    for i in range(10):
        process = mp.Process(target=do_requests2, args=(result_queue, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not result_queue.empty():
        process_id, status_code = result_queue.get()
        print(f'Process {process_id} => example.com: {status_code}')


def main3():
    threads = []
    result_queue = queue.Queue()
    for i in range(10):
        thread = threading.Thread(target=do_requests2, args=(result_queue, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    while not result_queue.empty():
        thread_id, status_code = result_queue.get()
        print(f'Thread {thread_id} => example.com: {status_code}')


def do_requests3(session):
    return session.get('https://example.com')


async def main4():  # coroutine: pause and resume
    async with aiohttp.ClientSession() as session:  # an object has __aenter__ and __aexit__ method.  # optional in async def
        tasks = []
        for _ in range(0, 10):
            tasks.append(do_requests3(session))

        results = await asyncio.gather(*tasks)  # object must has __await__ method (generator), e.g. async def, Task, Future  # vital in async def
                                                # switch to do the other things after touches await and switch back when yield !
                                                # asyncio.gather.gather is similar as wait and join
        for r in results:
            print('example.com =>', r.status)


if __name__ == '__main__':
    # naive, 5.3s
    start = time.time()
    main1()
    print("Naive", 'Elapsed time:', time.time() - start, "\n")

    # multiprocessing, 0.58s, memory inefficient
    start = time.time()
    main2()
    print("multiprocess", 'Elapsed time:', time.time() - start, "\n")

    #threading, 0.56s, memory efficient
    start = time.time()
    main3()
    print("threading", 'Elapsed time:', time.time() - start, "\n")

    # asyncio, 0.56s, memory efficient
    start = time.time()
    asyncio.run(main4())  # ayncio.run() execute coroutine by "event loop"
    print("asyncio", 'Elapsed time:', time.time() - start)


"""
# Another simplest asyncio

import asyncio

class CustomAwaitable:
    def __init__(self, value):
        self.value = value

    def __await__(self):
        # Simulate asynchronous behavior
        print("Start awaiting...")
        yield  # This allows control to return to the event loop
        print("Finished awaiting.")
        return self.value  # Final result


async def main():
    obj = CustomAwaitable(42)
    result = await obj
    print(f"Result: {result}")

asyncio.run(main())
"""


"""
# Another more more simple,
# usually awaitable object (asyncio.sleep) is already the api interface (don't need to implement)

import asyncio
import time
from typing import List


def add1_sync(a: int):  # cost heavy operation
    time.sleep(1)
    return a + 1


def main1(n: int) -> List[int]:
    results = [add1_sync(i) for i in range(n)]
    return results


async def add1_async(a: int):  # cost heavy operation
    await asyncio.sleep(1)  # awaitable object usually be a api call
    return a + 1


async def main2(n: int):
    tasks = [
        asyncio.create_task(add1_async(i))
        for i in range(n)
    ]
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    start = time.time()
    res = main1(5)
    print(time.time() - start)  # 5 seconds
    print(res)
    
    start = time.time()
    res = asyncio.run(main2(5))
    print(time.time() - start)  # 1 second
    print(res)
"""

