x = 5
y = 8
z = 5

if x < y and x == z: # after : Thonny (and other editors) will auto indent 4 spaces
    print('I am in the if block')
    print('as am I!')
print('I am not in the if block') # use shift-tab to dedent out of the if block

if x > y or x != z:
    print('inside') # this statement will not print because neither x > y or x!=z is True
print('outside') # this statement will print because it is not in the if block