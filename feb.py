def fibonacci(n):
    fib_series = [0, 1]  
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])  
    return fib_series
n=int(input(" Enter the number n:-"))
result = fibonacci(n)
print("Fibonacci series of length", n, ":", result)
