num = int(input("Digite um número em decimal: "))

binary_num = ''

if num == 0:
    binary_num = '0'

while num > 0:
    binary_num = str(num % 2) + binary_num
    num //= 2

print(binary_num)

# num = input("Digite um número em binário: ")

# decimal_num = 0

# exp = 0

# for n in reversed(num):
#     decimal_num += int(n) * (2 ** exp)
#     exp += 1

# print(decimal_num)