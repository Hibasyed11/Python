import turtle 
t=turtle.Turtle()
turtle.Screen().bgcolor("lavender")
turtle.Screen().setup(200,200)
t.speed(0)
colors=["red", "green", "blue", "yellow"]
size=50
for i in range (5):
    for j in range (5):
        t.penup()
        t.goto(j*size,i*size)
        t.pendown()
        t.fillcolor(colors[(i+j)% len(colors)])
        t.begin_fill()
        for k in range (4):
            t.forward(size)
            t.right(90)
        t.end_fill()
turtle.done()