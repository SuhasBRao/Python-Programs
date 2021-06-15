import cmath

my_inpt = input()
my_cmplx = complex(my_inpt)
polar = cmath.polar(my_cmplx)
print(*polar,sep='\n')
