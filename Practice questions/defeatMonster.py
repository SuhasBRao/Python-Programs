
#print(mst, bonus)

def max_dft(ex,mst,bonus):
    mst = dict(zip(mst,bonus))
    #print(mst)
    no_times_defeat = 0
    anyMnstr = [x for x in mst if x <= ex]
    while anyMnstr:
        
        #print(anyMnstr)
        if anyMnstr:
            ex += mst.pop(anyMnstr[0])
            no_times_defeat +=1
        anyMnstr = [x for x in mst if x <= ex]

    print(no_times_defeat)

if __name__ =='__main__':
    no_monster = int(input())
    ex = int(input())
    mst = []
    bonus = []
    for i in range(no_monster):
        mst.append(int(input()))

    for i in range(no_monster):
        bonus.append(int(input()))
    
    max_dft(ex,mst,bonus)