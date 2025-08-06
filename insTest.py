lst = [1,3,2,7,4]

def insTest(lst):
    for i in range(1,len(lst)):
        j = i-1
        while j>=0 and lst[j]<lst[i]:
            if