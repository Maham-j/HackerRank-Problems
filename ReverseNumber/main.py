"""1st method"""

num = int(input())
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))




"""second method"""
num = 123456
print(str(num)[::-1])
