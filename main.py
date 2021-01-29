# Indian_flag in python by Smrutiofficial.com
import turtle
import time

# turtle as smruti
smruti = turtle.Turtle()

smruti.speed(100)
smruti.penup()
# decide the shape of cursor/turtle
smruti.shape("turtle")

# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height/3
stripe_width = flag_width

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height / 2


def draw_fill_rectangle(x, y, height, width, color):
    smruti.goto(x,y)
    smruti.pendown()
    smruti.color(color)
    smruti.begin_fill()
    smruti.forward(width)
    smruti.right(90)
    smruti.forward(height)
    smruti.right(90)
    smruti.forward(width)
    smruti.right(90)
    smruti.forward(height)
    smruti.right(90)
    smruti.end_fill()
    smruti.penup()


# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 3 stripes, 1 saffron, 1 white and 1 green
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    # decrease value of y by stripe_height
    y = y - stripe_height   
    # create middle white stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    # create last green stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height


def draw_chakra():
    smruti.speed(1)
    smruti.goto(0,0)
    color = "#000080" # navy blue
    smruti.penup()
    smruti.color(color)
    smruti.fillcolor(color)
    smruti.goto(0, 0 - chakra_radius)
    smruti.pendown()
    smruti.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        smruti.penup()
        smruti.goto(0,0)
        smruti.left(15)
        smruti.pendown()
        smruti.forward(chakra_radius)
  
    

# start after 5 seconds.
time.sleep(0)
# draw 3 stripes
draw_stripes()
# draw squares to hold stars
draw_chakra()
# hide the cursor/turtle
smruti.hideturtle()
screen.mainloop()
