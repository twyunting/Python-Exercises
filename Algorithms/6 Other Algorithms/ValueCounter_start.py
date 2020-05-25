# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
dic = {}

# TODO: iterate over each item and increment the count for each one
for i in items:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

# print the results
print(dic)
