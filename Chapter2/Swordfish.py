while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello Joe, what is the pasword? (It is a fish.)")
    password = input()
    if password == "Swordfish":
        break
print("Acces granted.")
