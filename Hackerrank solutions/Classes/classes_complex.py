'''
Problem statement -> https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
'''
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.c_number = complex(real,imaginary)
        self.result_real = None # variables for printing
        self.result_imaginary = None

        
    def __add__(self, no):
        res = self.c_number + no.c_number
        self.result_real = res.real
        self.result_imaginary = res.imag
        return self.__str__()

        
    def __sub__(self, no):
        res = self.c_number - no.c_number
        self.result_real = res.real
        self.result_imaginary = res.imag
        return self.__str__()

    def __mul__(self, no):
        #self.result_real,self.result_imaginary = self * no
        
        res = self.c_number * no.c_number
        self.result_real = res.real
        self.result_imaginary = res.imag
        #print(self.__str__())
        return self.__str__()

    def __truediv__(self, no):
        res = self.c_number / no.c_number
        self.result_real = res.real
        self.result_imaginary = res.imag
        return self.__str__()

    def mod(self):
        res = abs(self.c_number)
        self.result_real = res.real
        self.result_imaginary = res.imag
        return self.__str__()

    def __str__(self):
        if self.result_imaginary == 0:
            result = "%.2f+0.00i" % (self.result_real)

        elif self.result_real == 0:
            if self.result_imaginary >= 0:
                result = "0.00+%.2fi" % (self.result_imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.result_imaginary))

        elif self.result_imaginary > 0:
            result = "%.2f+%.2fi" % (self.result_real, self.result_imaginary)
        else:
            result = "%.2f-%.2fi" % (self.result_real, abs(self.result_imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')