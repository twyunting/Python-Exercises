def quicksort(array):
    if len(array) < 2:  #<2 equal <=1
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array [1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,23,234,556,455666,2,667,69]))