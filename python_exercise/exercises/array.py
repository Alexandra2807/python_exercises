#create an array of 5 integers and display the array items. Access individual element through indexes.
from array import *

array_num = array('i', [1,5,6,8,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])