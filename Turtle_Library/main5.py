# import turtle library
import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
# my_pen.speed(0)   # Turtle'nin çizim hızını ayarla (0 en hızlı, 1 en yavaş)
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
