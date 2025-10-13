import turtle 
t=turtle.Turtle()
turtle.Screen().bgcolor("black")
turtle.Screen().setup(200,200)
t.speed(0)
colors=["red", "orange", "yellow", "green", "blue", "violet" ]
for i in range(36):
   t.color(colors[i % len(colors)])
   t.penup()
   t.goto(0,0)
   t.pendown()
   for j in range (6):
      t.forward(50)
      t.right(60)
   t.right(10)
turtle.done()
