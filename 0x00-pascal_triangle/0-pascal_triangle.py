#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
  """
  find the pascal triange from a given integer size
  """
  list1 = []
  list2 = []
  for i in range(n):
    list1.append([])
    list1[i].append(1)  
    for j in range(1, i):  
      list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
    if(n != 0):  
      list1[i].append(1)
    list2.append(''.join(list1[i]))
    return list2

