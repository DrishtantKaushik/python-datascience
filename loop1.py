from turtle import *
speed('fastest')
pencolor('red')
pensize(6)

for i in range(6):
  fd(120)
  rt(60)
  write(f'n={i}', font=("Consolas" ,16))

hideturtle()
mainloop()
