import figures
import turtle

# Set up the screen and turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)

figures.move(pen, -300, 0)
figures.draw_square(pen, 100)

figures.move(pen, -100, -100)
figures.draw_triangle(pen, 100)

figures.move(pen, 100, -100)
figures.draw_rectangle(pen, 200, 100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
