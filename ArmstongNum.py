# Write a program to check if the number entered by the user is an Armstrong number or not

# take input from a user
num = int(input("Enter a number:"))

# initalize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstong number")

    