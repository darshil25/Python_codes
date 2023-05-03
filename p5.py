cube = lambda x: x ** 3

def fibonacci(n):
    
    # creating the list of first two items
    fib = [0, 1]
    
    # using list comprehension
    [fib.append(sum(fib[-2:])) for x in range(n)]
    return fib[:n]
              
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))