while True:
    print("Who are you?")
    if input() != "Joe":
        continue
    print("Hello Joe, what is the pasword? (It is a fish.)")
    if input() == "Swordfish":
        break
print("Acces granted.")
