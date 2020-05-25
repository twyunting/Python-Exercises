# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        midIdx = (upperIdx + lowerIdx) // 2
        if itemlist[midIdx] == item:
            return midIdx
        if item > itemlist[midIdx]:
            lowerIdx = midIdx + 1
        else:
            upperIdx = midIdx - 1
    
    if lowerIdx > upperIdx:
        return None

        # TODO: calculate the middle point


        # TODO: if item is found, return the index


        # TODO: otherwise get the next midpoint


    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
