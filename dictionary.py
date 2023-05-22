
dictionary_wether = {'Mon': 12, 'Tue' : 15, 'Weth' : 20, 'Thur': 21}

dictionary_wether_c = { k :((32 - v)*5/9).__round__(2)  for k, v in dictionary_wether.items() }
print(dictionary_wether_c)

#(32 °F − c) × 5/9 = 0 °C
#weather_c = {'Mon':12, 'Tue':14, 'Wed':15, #####}
#then convert this centigrade dictionary into
#fehrenheit dictionary using dictionary comprehensi
###
# print(a_dict.values())
#print(a_dict.items())
#b_dict = {k : v*2 for k,v in a_dict.items()}
#print(b_dict)
#5! = 5*4*3*2*1

#3! = 3*2*1
'''
3! = 3 * (3-1)!
3! = 3*2!

((((2! = 2 * (2-1)!))))
((((2! = 2 * 1!(func)))))

((1! = 1 * (1-1)!))
((1! = 1 * 0!(func)))
'''

#1! = 1
#0! = 1

#Factorial
#Using Recursion

def factorial(n):
    if n < 1:
        return 1
    else:
        return n*factorial(n-1)

factorial(5)
print(factorial(5))


#lista = [2,3,4]

#print(lista[0])
#print(lista[1:3])
lista = [2,3,4]
def sum(lista):
    if len(lista) == 1:
        return lista[0]
    else :
        return lista[0] + sum(lista[1::])
print(sum(lista))



