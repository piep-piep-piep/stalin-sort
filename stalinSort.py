#!/usr/bin/python

def sort(inputlist):
    outputlist = []
    for index, item in enumerate(inputlist):
        if index == 0:
            outputlist.append(item)
        elif item > outputlist[-1]:
            outputlist.append(item)
    return(outputlist)

# inputlist1 = [1, 3, 5, 7, 2, 4, 4, 56, 26, 562, 5346, 234546]
# sort(inputlist1)
