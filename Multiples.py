number = int(input("Enter a number : "))
result = ""
if number % 3 == 0:
    result = str(number) + " is multiple of 10"
else:
    result = str(number) + " is not multiple of 10"
print(result)