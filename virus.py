import turtle
obj = turtle.Turtle()
obj.speed(0)
obj.pencolor("Red")
#obj.bgcolor

win = turtle.screensize()
turtle.bgcolor("black")
turtle.title("AjeetK")
f = 0
r = 0
obj.up()
obj.goto(0,300)
obj.down()
while(1):
    obj.forward(f)
    obj.right(r)
    f+=3
    r+=1
    if r >= 200:
        break
#obj.hideturtle()
turtle.done()
