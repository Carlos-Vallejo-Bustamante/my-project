saludo = 'Hola mundo'
print(saludo)

pedir_nombre = input('Ingresa tu nombre')

saludo_con_nombre = f'Hola {pedir_nombre}'

print(saludo_con_nombre)

total = pow((3+2)/(2*5),2)
sum = ((3+2)/(2*5))**2
print(total, sum)

## FIZZBUZZ

FIZZ = 'Fizz'
BUZZ = 'Buzz'

for multiple in range(101):
    if multiple % 3 == 0 and multiple % 5 == 0:
        print(f'{FIZZ}{BUZZ}')
    elif multiple % 3 == 0:
        print(FIZZ)
    elif multiple % 5 == 0:
        print(BUZZ)
    else:
        print(multiple)


