num = int(input("Enter a number: "))
if num % 7 == 0:
    print(num, "is divisible by 7")
elif num % 7 != 0:
    print(num, "is not divisible by 7")
else:
    print("Invalid input")