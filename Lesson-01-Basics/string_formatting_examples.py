text = '{}'.format('hello')
print(text)

text = '{} world of {}'.format('Hello', 'python')
print(text)

text = 'xx{:10}xx'.format('stuff')
print(text)

text = 'xx{:>10}xx'.format('right')
print(text)

text = 'xx{:0>10}xx'.format('right')
print(text)

text = 'xx{:^12}xx'.format('center')
print(text)

num = '{:d}'.format(42)
print(num)

num = '{:02d}'.format(4) # force 2 digits zero pad
print(num)

import math
floating_num = '{:f}'.format(math.pi)
print(floating_num)

import math
floating_num = '{:.2f}'.format(math.pi)
print(floating_num)