import turtle

# Initialize window
window = turtle.Screen();

# Initialize turtle
my_turtle = turtle.Turtle();
my_turtle.speed(4);

my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

# Initialize constants
FULL_TURN = 360.0
HALF_TURN = FULL_TURN/2

# Initialize variables
distance = 400
angle = HALF_TURN * (9.0/10.0)
iterations = 20

# Run program
for _ in range(iterations):
	my_turtle.forward(distance)
	my_turtle.right(angle)

turtle.done()
