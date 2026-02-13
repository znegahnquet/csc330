import time
from multiprocessing import Process

# PROVIDED FUNCTION — DO NOT MODIFY
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Worker function (same idea as lecture example)
def worker(n):
    result = fib(n)
    print(f"fib({n}) = {result}")

if __name__ == "__main__":
    nums = [35, 36, 37, 38, 39]

    processes = []

    start_time = time.time()

    # Create and start processes
    for n in nums:
        p = Process(target=worker, args=(n,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    end_time = time.time()

    elapsed = end_time - start_time
    print("Total elapsed time:", elapsed, "seconds")