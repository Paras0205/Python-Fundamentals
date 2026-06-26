fruits: list[str] = ["mango","banana","apple"]

fruits.append("grapes")     # add to end → ['mango','banana','apple','grapes']
fruits.insert(1,"guava")    # add at position 1
fruits.remove("banana")     # remove by value
fruits.pop()                # remove last, returns it
fruits.pop(0)               # remove by index
fruits.sort()               # sort ascending (modifies in place)
fruits.sort(reverse=True)   # sort descending
fruits.reverse()            # flip the list
fruits.count("mango")       # how many times value appears
fruits.index("apple")       # position of value
fruits.clear()              # empty the list
fruits.extend("Orange")     #add orange in list       

# Check membership
print("mango" in fruits)    # True or False