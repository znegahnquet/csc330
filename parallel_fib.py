import os
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

nums = [35, 36, 37, 38, 39]

start_time = time.time()

for n in nums:
    pid = os.fork()

    if pid == 0:
        result = fib(n)
        print(f"fib({n}) = {result} (PID {os.getpid()})")
        os._exit(0)

for _ in nums:
    os.wait()

end_time = time.time()

elapsed = end_time - start_time
print(f"Total elapsed time (parallel): {elapsed:.2f} seconds")