people = int(input("How many are you there : "))
message = ""
if people > 8:
    message = "You have to wait for the table"
else:
    message = "The table is ready"
print(message)