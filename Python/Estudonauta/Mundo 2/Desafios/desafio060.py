num = int(input('Digite um numero: '))
temp = num
fat = num
while temp > 1:
    print(temp, 'x')
    fat = fat * (temp - 1)
    temp -= 1

print("O fatorial de {} é :{}".format(num, fat))
