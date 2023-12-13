
while True:
    try:
        number = int(input("Enter a phone number "))
    except ValueError:
        pass
    else:
        break

persons = [
    {"name":"john","phone": 100},
    {"name":"frank","phone": 102},
    {"name":"bright","phone": 104},
    {"name":"bob","phone": 106,},
    {"name":"mike","phone": 108}
]


for person in persons:
    if person["phone"] == number:
        print(person["name"], person["phone"], sep=", ")
        break
    

    