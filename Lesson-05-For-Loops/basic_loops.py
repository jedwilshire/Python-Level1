for i in range(5):
    print('hello') # this will print 5 times
    

# all code in for 'block' is repeated
for i in range(3):
    print('python', end = ' ')
    print('rocks')
print('goodbye')

for k in range(10, 19, 3):
    print(k)

x = 10
while x > 0:
    print(x, end = '  ')
    x -= 1


while True:
    command = input('what is your bidding')
    if command == 'STOP':
        break
