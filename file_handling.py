import random

file = open('my_file.txt', mode='a')
file.write('Hello I am Jerry\n')
file.close()
num = random.randint(0, 10)

reading_file = open('my_file.txt', mode='r')
content = reading_file.readlines()
print(content[num])

file = open('my_file1.txt', mode='w')
for i in range(100):
        mynum = random.randint(0, 100)
        file.write(f'{mynum}\n')
file.close()

file = open('my_file2.txt', mode='w')
for i in range(100):
        mynum = random.randint(0, 100)
        file.write(f'{mynum}\n')
file.close()










