import turtle
wn = turtle.Screen()
wn.bgcolor("light green")

bo = turtle.Turtle()
bo.up()
bo.shape("turtle")
bo.color("blue")
bo.pensize("5")


for num in range(1,100):
	bo.forward(num)
	bo.right(num)
	
wn.exitonclick()