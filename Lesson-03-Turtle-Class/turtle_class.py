from turtle import Turtle

hank = Turtle()
hank.shape('turtle')
hank.color('purple')
hank.forward(120)

jill = Turtle()
jill.shape('square')
jill.color('green')
jill.left(135)
jill.forward(100)

print(hank.xcor(), hank.ycor())
print(hank.isdown())
hank.penup()
print(hank.isdown())


hank.name = 'Hank'
hank.is_turtle = True
print(hank.name, hank.is_turtle)

jill.name = 'Jill'
jill.is_turtle = False
print(jill.name, jill.is_turtle)