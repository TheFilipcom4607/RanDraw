import turtle
import random

# Define a function for generating shapes
def generate_shape():
    turtle.clear() # Clear the previous shape
    turtle.color(random.choice(colors))
    turtle.begin_fill() # Fill the shape with color
    
    # Generate random shape parameters
    shape_size = random.randint(25, 50)
    number_of_sides = random.randint(4, 20)
    angle = 360 / number_of_sides
    curvature = random.uniform(1, 50)
    
    # Draw the shape
    turtle.right(random.uniform(0, 360))
    for j in range(number_of_sides):
        turtle.forward(shape_size)
        turtle.right(angle + curvature)
        curvature *= -1
    
    turtle.end_fill() # Finish filling the shape with color

# Configure the turtle
turtle.speed('fastest')
turtle.pensize(2)
turtle.colormode(255)

# Define colors
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Generate the initial shape
generate_shape()

# Attach the function to the "q" key press event
turtle.listen()
turtle.onkey(generate_shape, 'q')

# Close the window when the "Escape" key is pressed
turtle.onkey(turtle.bye, 'Escape')
turtle.mainloop()
