import hcf
def lcm(x,y):
    lcm = (x*y)//hcf.hcf(x,y)
    return lcm

if __name__=='__main__':
    print(lcm(7,6))
