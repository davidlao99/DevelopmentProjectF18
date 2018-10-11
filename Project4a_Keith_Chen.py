
ARRAY_SIZE = 8500

for i in range(0,ARRAY_SIZE):
    f = open("randomInts.txt", "r")
    randomList = []
    for line in f:
        randomList.append(line)
print(randomList)

def merge_sort(inList,left,right):
  if(left < right):
    mid = (left + (right - 1)) // 2
    merge_sort(inList,left,mid)
    merge_sort(inList,mid+1,right)
    merge(inList,left,mid,right)
    
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 

    L = [0] * int((n1)) 
    R = [0] * int((n2)) 

    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 

    i = 0
    j = 0
    k = l
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1

    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

dividedList = []
for i in range (0,ARRAY_SIZE//500):
  dividedList.append(randomList[i*500:(i + 1)*500])
  merge_sort(dividedList[i],0,len(dividedList[i])-1)
  print(dividedList[i])
