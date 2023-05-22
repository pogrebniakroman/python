#list comprehension
my_name = 'Roman'

list_name = [i for i in my_name]
print(list_name)
for i in list_name:
    print(i)
#iterated list
#create a list of first 10 natural numbers
list_name
num_list=[]
for i in range(10):
    num_list.append(i)

#print(num_list)

#Single line of code
#num_list = [new_item for item in list]

lista = [i for i in range(20)]
print(lista)

#Store your name inside a variable
#iterate through your name
#and
#print it letter by letter

#R
#o
#m
#a
#n

#using List_comprehension

numbers = [1, 2, 3]

aded_numbers = [i * 2 for i in numbers]
print(aded_numbers)

two_list = [i * 2 for i in range(6)]
print(two_list)


name_list = ['Roman', 'Abdul', 'Aziz', 'Ivan']
name_list_max = [i for i in name_list if len(i) > 4]
print(name_list_max)

num_list = [1,1,1,2,3,5,4,7,46,45,7,4,6,11,23,24,27,11,13,12]

#Go through this num_list
#check which number is even
#only add those numbers to the new_even_list

new_even_list = [ i for i in num_list if i % 2 == 0]
print(new_even_list)

x = 7
if x > 2 :
    print('Value bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i < 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')


if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print ('All done')

x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')