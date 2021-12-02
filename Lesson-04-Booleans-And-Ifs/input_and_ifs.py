name = input('What is your name')
if name == 'Jed':
    print('That\'s my name too!')
    
num = int(input('What is your favorite number?'))
if num == 7:
    print('That is my favorite number too!')

grade = int(input('What score did you get on the quiz?'))
if grade >= 70:
    print('You passed!')
else:
    print('Oops - you failed this quiz.')


age = int(input('How old are you?'))
if age < 42:
    print('You are younger than me')
elif age == 42:
    print('You are my age.')
else:
    print('You are older than me.')