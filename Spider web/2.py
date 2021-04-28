N = int(input())

def fibonacci(num):
    my_list = []
    num1 = 1
    num2 = 3
    series = 0
    my_list = [num1,num2]

    for _ in range(num - 2):
        #print(series, end=' ')
        series = num1 + num2
        num1 = num2
        num2 = series
        my_list.append(series)
        #print(series, end=' ')
    return my_list
temp = fibonacci(N)
val = temp[N-1]
print(val % (10**9 + 7))