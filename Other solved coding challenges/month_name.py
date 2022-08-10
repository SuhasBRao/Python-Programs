n = int(input())
month_names = {1:'January', 2:'Febraury',3:'March', 4:'April',
                5:'May',6:'June', 7:'July', 8:'August',
                9:'September',10:'October', 11:'November', 12:'December'}
if 1<= n <= 12:
    print(month_names[n])
else:
    print('invalid input')