import turtle
import random

# Define function to generate shape
def generate_shape():
    turtle.clear() # Clear the previous shape
    turtle.color(random.choice(colors))
    turtle.begin_fill() # Fill shape with color
    
    # Randomize shape parameters
    shape_size = random.randint(25, 100)
    shape_sides = random.randint(5, 10)
    shape_angle = 360 / shape_sides
    shape_curvature = random.uniform(1, 50)
    
    # Draw shape
    turtle.right(random.uniform(0, 360))
    for j in range(shape_sides):
        turtle.forward(shape_size)
        turtle.right(shape_angle + shape_curvature)
        shape_curvature *= -1
    
    turtle.end_fill() # End shape fill

# Set up turtle
turtle.speed('fastest')
turtle.pensize(2)
turtle.colormode(255)

# Define colors
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Generate initial shape
generate_shape()

# Bind function to "q" key press event
turtle.listen()
turtle.onkey(generate_shape, 'q')

# Exit turtle when "Escape" key is pressed
turtle.onkey(turtle.bye, 'Escape')
turtle.mainloop()
