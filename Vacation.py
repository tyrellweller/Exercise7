places = {}
country = ""
visit = ""
active = True
while active:
    country = input("What country would you like to visit : ")
    visit = input("If you arrive in " + country + "where do you wanna go : ")
    places[country] = visit
    repeat = input("Would you like to add again : ")
    if repeat == 'no':
        break
for count , vis in places.items():
    print("\nI will visit " + count + " country")
    print("and i will go to the " + vis)