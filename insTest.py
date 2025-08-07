lst = [1,3,2,7,4]

def insTest(lst):
    for i in range(1,len(lst)):
        j = i-1
        while j>=0 and lst[j]>lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

            j -= 1
    return lst

print(insTest(lst))