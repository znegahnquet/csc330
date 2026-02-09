import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

nums = [35, 36, 37, 38, 39]

start_time = time.time()

for n in nums:
    result = fib(n)
    print(f"fib({n}) = {result}")

end_time = time.time()

elapsed = end_time - start_time
print(f"Total elapsed time (serial): {elapsed:.2f} seconds")