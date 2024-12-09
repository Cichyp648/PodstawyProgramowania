def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

def draw_rectangle(t, length_a, length_b):
    for _ in range(2):
        t.forward(length_a)
        t.left(90)
        t.forward(length_b)
        t.left(90)

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
