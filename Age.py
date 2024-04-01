age = int(input("How old are you : "))
price = 0
message = "$"
active = True
while age != 999:
    if age < 3:
        price = 0
    elif age >= 3 and age <= 12:
        price = 10
    else:
        price = 15
    age = int(input("How old are you : "))
if price == 0:
    message = "the ticket is free"
else:
    message += str(price)
print(message)