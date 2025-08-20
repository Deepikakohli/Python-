num = int(input("Enter a number: "))
last_digit = abs(num) % 10
if num % 3 == 0 and last_digit == 4:
    print(num, "is divisible by 3 and its last digit is 4")
else:
    print(num, "does not satisfy both conditions")