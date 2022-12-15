import turtle

pen = turtle.Turtle()
turtle.Screen().bgcolor("purple")
pen.pensize(6)

#huruf D
pen.up()
pen.goto(-10,250)
pen.down()
pen.pencolor("white")
pen.right(90)
pen.forward(135)

pen.up()
pen.goto(-10,250)
pen.down()
pen.right(-90)
pen.circle(-70,180)

#angka
pen.up()
pen.goto(-200,70)
pen.down()
pen.circle(50)
pen.up()
pen.goto(-151,30)
pen.down()
pen.left(90)
pen.forward(120)
pen.right(90)
pen.forward(100)

pen.up()
pen.goto(-40,70)
pen.down()
pen.right(180)
pen.circle(-80,180)
pen.left(180)
pen.forward(140)

pen.up()
pen.goto(200,70)
pen.down()
pen.circle(-20,180)
s = turtle.Screen().exitonclick()