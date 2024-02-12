from turtle import *

speed('fast')

s = 0
while s < 125:
    fd(50 + s)
    lt(60)
    write(s)
    dot(10)
    s += 5
hideturtle()
mainloop()
    
    