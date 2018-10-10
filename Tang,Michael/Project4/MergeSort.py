##Name: Michael Tang
##Project #4
## Description: Utilize merge sort to sort a large amount of data

list1 = []
rd =open("C:/Users/Miko/DevelopmentProjectF18/Tang,Michael/Project4/randomInts.txt", "r")

for line in rd.readlines():
    for i in line.split():
        list1.append(int(i))
        
def MergeSort(list):

    if len(list)>1:
        mid=len(list)//2
        leftSide=list[:mid]
        rightSide=list[mid:]

        MergeSort(leftSide)
        MergeSort(rightSide)

        a=0
        b=0
        c=0

        while a < len(leftSide) and b < len(rightSide):
            if leftSide[a] < rightSide[b]:
                list[c] = leftSide[a]
                a+=1
            else:
                list[c] = rightSide[b]
                b+=1

            c+=1

        while a < len(leftSide):
            list[c]=leftSide[a]
            a+=1
            c+=1

        while b < len(rightSide):
            list[c]=rightSide[b]
            b+=1
            c+=1

MergeSort(list1)
print(list1)
