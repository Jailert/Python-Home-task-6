# Задача на фиббоначи через map.

k = int(input('Enter k = '))
fib = [0, 1]
list(map(lambda i: fib.append(fib[i-2] + fib[i-1]), range(2, k + 1)))
negfib = [0, 1]
list(map(lambda i: negfib.append(negfib[i-2] - negfib[i-1]), range(2, k + 1)))
negfib.remove(0)
negfib = list(reversed(negfib))
print(negfib + fib)
