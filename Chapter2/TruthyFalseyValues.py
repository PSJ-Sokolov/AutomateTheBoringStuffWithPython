#There are some values that are considered Truth like or False like.
#FALSE: 0, 0.0, '', False.
#Let us demonstrate!:

name = ''
while not name:                                              #Will stop when not falsoid.
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numberOfGuests = input()
if numberOfGuests:                                           #Will trigger when not 0 ,0.0 ,'' ,or nil.
    print('be sure to have enough room for all your guests.')
print('Done')
