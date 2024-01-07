import turtle as t
import colorsys
t.tracer(2)
t.pensize(2)
h=0.5
t.bgcolor('black')
for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.004
    t.pencolor(c)
    t.fd(i)
    t.rt(80)
    t.fd(i)
    t.rt(120)
    t.fd(i)
    t.rt(180)
    t.fd(i)
    t.rt(240)
    t.fd(i)
    t.rt(300)
    t.fd(i)
    t.rt(360),
t.done()

