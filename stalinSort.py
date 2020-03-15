def sort(inputlist):
    outputlist = []
    for index, item in enumerate(inputlist):
        if index == 0:
            outputlist.append(item)
        elif item > outputlist[-1]:
            outputlist.append(item)
    return(outputlist)