#Jose Garcia
#AI_Project4

#section that performs the merge sort
def mergeSort(thislist):
    if len(thislist) > 1:
        mid = len(thisList)//2
        leftList = thisList[:mid]
        rightList = thisList[mid:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                thisList[k] = leftList[i]
                i = i + 1
            else:
                thisList[k] = rightList[j]
                j = j + 1
            k = k + 1

        while i < len(leftList):
            thisList[k] = rightList[j]
            j = j + 1
            k = k + 1
        

main():
    listSize = 8500
    fileName = open("randomInts.txt", "r")
    numbers = []
    for line in fileName:
        numbers.append(line)
    list2 = []
    for i in range(0, arraySize//500):
        list2.append(randomList[i*500:(i + 1)*500])
        mergeSort(list2[i],0,len(list2[i])-1)
        print(list2)
