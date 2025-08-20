num = int(input("Enter a number: "))
last_digit = abs(num) % 10
if num % 7 == 0 or last_digit == 5:
    print(num, "is divisible by 7 or its last digit is 5")
else:
    print(num, "is not divisible by 7 and its last digit is not 5")