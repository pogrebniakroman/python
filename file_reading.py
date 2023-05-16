import random

reading_file1  = open('my_file1.txt', mode='r')
content1 = reading_file1.readlines()
print(content1)
reading_file1.close()

reading_file2  = open('my_file2.txt', mode='r')
content2 = reading_file2.readlines()
print(content2)
reading_file2.close()

content_list1 = []
content_list2 = []

common_list = []
for i in content1:
    print('first', i)
    for j in content2:
        print('second', j)
        if  i == j:
            common_list.append(int(i))
print(common_list)

num_list = [1,1,1,2,3,5,4,7,46,45,7,4,6,11,23,24,27,11,13,12]

#Go through this num_list
#check which number is even
#only add those numbers to the new_even_list

x = 11
if x in num_list:
    print('Hurray')
else:
    print('Not available')

#after reading both the text files filled with numbers
#using list comprehension make a new_list of common numbers



common_list = []

new_num_list = [int(i) for i in content1  if i in content2]
print(new_num_list)

content1 = ['1','2','3']
content2 = ['2','4','5']

common_list = []

#Dictionary comprehension
#1# Generating a dictionary from a List
#2# Generating a dictionary from a dictionary

#dictionary is made of keys and values

a_list = ['Aziz','Beka','Steven','Abdul','Johnathan']

name_len_dictionary = {name : len(name) for name in a_list}
print(name_len_dictionary)

#Take a_list and give each student randomly chosen marks
#between 0,100 and make a dictionary out of it using
#dictionary comprehension

a_new_list_dict = {i : random.randint(0,100) for  i in a_list}
print(a_new_list_dict)


