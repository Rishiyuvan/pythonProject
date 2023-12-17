from array import *
numArr = array('i',[5,4,6,7])
temp =0
print ("Array values")
print()
print(numArr,end="")
for i in range(0,len(numArr)):
    for j in range(i+1,len(numArr)):
        if numArr[i]>numArr[j]:
            temp = numArr[i]
            numArr[i] = numArr[j]
            numArr[j] = temp
print()
print("After ascending")
print()
print(numArr,end="")
print("Demo purpose")


