def InsertSort(lst):
    for i in range(1,len(lst)):
        j = i-1
        while j>=0 and lst[j+1]<lst[j++]:
            temp = j+1
            lst[j+1] = lst[j]
            lst[j] = temp

            j-=1
    return lst 


print(InsertSort([3,4,5,8,1]))
