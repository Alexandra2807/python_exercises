'''
Created on Feb 14, 2020

@author: ameli
'''
#take a list and returns a new list with unique elements of the first list.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,2,2,3,6,7,9]))