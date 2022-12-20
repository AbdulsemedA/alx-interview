#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    find the pascal triange from a given integer size
    """
    if n <= 0:
        return []
    # empty list
    list1 = []
    #loop through n
    for i in range(n):
        #create a list inside list1
        list1.append([])
        #append first 1
        list1[i].append(1)
        for j in range(1, i):
            list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
        if(i != 0):
            list1[i].append(1)
    return list1
