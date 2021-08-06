'''
Implememt tower of hanoi using recursion.
'''
def hanoi(n,src,temp,dst):
    if n == 1:
        print(f'Move disk {n} from peg {src} to peg {dst}')
    else:
        hanoi(n-1, src,dst,temp)
        print(f'Move disk {n} from peg {src} to peg {dst}')
        hanoi(n-1,temp,src,dst)
n = int(input())
hanoi(n,'A','B','C')