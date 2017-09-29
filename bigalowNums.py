def findNums():
    nums = []
    for i in range(1,100):
        nums.append(6*i-1)
        nums.append(6*i+1)
    return nums

def findComposite():
    composNums = []
    for i in findNums():
        for j in xrange(5,int(i**0.5)+1,2):
            if i%j == 0:
                composNums.append((i,j,i/j))
                break
    for i in composNums:
        print i
        
