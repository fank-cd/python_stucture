#coding:utf-8
#不适用递归的求和
def listsum(numlist):
    thesum = 0
    for i in numlist:
        thesum = thesum + i
    return thesum
l = [1,3,5,7,9,]
print listsum(l)

def listsum1(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])
    
print listsum1(l)