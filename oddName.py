''' Jonah Burnaby '''

name = input('Enter your name')

if name.isspace()!= True:
    print(name[1::2].replace(' ',''))
else:
    print('Name is not valid, please enter a string')
