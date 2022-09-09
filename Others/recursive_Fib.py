"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position, memo ={}):
    if position in memo:
        return memo[position]
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        memo[position] = get_fib(position-1,memo) + get_fib(position-2, memo)
        return memo[position]
    #return -1

# Test cases
print(get_fib(4))
print(get_fib(5))
print(get_fib(50))
