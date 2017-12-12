####This program says hello and asks for my name.
print("Hello world!")                                       ##Print hello world to the screen.
print("What is your name?")                                 ##Ask for their name.
myName = input()                                            ##Get their name; put it in var myName
print("It is good to meet you, " + myName)                  ##Greet them.
print("The length of your name is:")                        ##Print the length of their name.
print(len(myName))                                          ##^
print("What is your age?")                                  ##Ask for their age.
myAge = input()                                             ##Get their age.
print("You will be " + str(int(myAge) + 1)) + " in a year!" ##State a trivial message: saying they will be one year older, in one year.
