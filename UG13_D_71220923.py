import turtle

pen = turtle.Turtle()
turtle.Screen().bgcolor("violet")
pen.pensize(6)

#huruf D
pen.up()
pen.goto(-10,270)
pen.down()
pen.pencolor("gold")
pen.right(90)
pen.forward(135)

pen.up()
pen.goto(-10,270)
pen.down()
pen.right(-90)
pen.circle(-70,180)

#angka 9
pen.up()
pen.goto(-200,90)
pen.down()
pen.circle(50)
pen.up()
pen.goto(-151,50)
pen.down()
pen.left(90)
pen.forward(120)
pen.right(90)
pen.forward(100)

#angka 2
pen.up()
pen.goto(-40,90)
pen.down()
pen.right(180)
pen.circle(-78,180)
pen.left(180)
pen.forward(140)

#angka 3
pen.up()
pen.goto(200,110)
pen.down()
pen.circle(-50,180)
pen.left(180)
pen.circle(-50,180)

#huruf P
pen.up()
pen.goto(-10,-270)
pen.down()
pen.right(90)
pen.forward(145)
pen.right(90)
pen.circle(-40,180)
s = turtle.Screen().exitonclick()