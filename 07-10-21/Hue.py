def bubblesort (mlist):
    temp = 0
    for i in range(0,len(mlist)):
        for j in range(0,len(mlist)-1):
            if mlist[j] > mlist[j+1]:
                temp = mlist[j]
                mlist[j] = mlist[j+1]
                mlist[j+1] = temp
    return mlist
def insertionsort (mlist):
    temp = 0
    for i in range(0,len(mlist)):
        temp = mlist[i]
        j = i
        while j > 0 and mlist[j-1] > temp:
            mlist[j] = mlist[j-1]
            j = j-1
        mlist[j] = temp
    return mlist
def selectionsort (mlist):
    for i in range(0,len(mlist)-1):
        for j in range(i+1,len(mlist)):
            if mlist[i] > mlist[j]:
                temp = mlist[i]
                mlist[i] = mlist[j]
                mlist[j] = temp

    return mlist
if __name__ == "__main__":
    alist = [6, 2, 5, 3, 3, 7, 1, 6, 9, 2, 5]
    bsortlist = bubblesort(alist.copy())
    isortlist = insertionsort(alist.copy())
    ssortlist = selectionsort(alist.copy())
    print(bsortlist)
    print(isortlist)
    print(ssortlist)