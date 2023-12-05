myNumbers = [4, 6, 9, 12, 22, 22, 27, 33, 17]
print("Original List:",myNumbers)

for j in range (0,8):

    for i in range (0,8):
        if (myNumbers[i]>myNumbers[i+1]):
            z=myNumbers[i+1]
            myNumbers[i+1]=myNumbers[i]
            myNumbers[i]=z


print(myNumbers)
