nums = input('Digite um numero: ')
num = int(nums)
milhar = num // 1000
centena = num % 1000
dezena = centena % 100
unidade = dezena % 10
dezena //= 10
centena //= 100
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')
print('=' * 29)
print(f'Milhar: {nums[0]}')
print(f'Centena: {nums[1]}')
print(f'Dezena: {nums[2]}')
print(f'Unidade: {nums[3]}')

