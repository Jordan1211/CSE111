"""
During this prove milestone and the next prove assignment, 
you will write a Python program that draws a semi-realistic 
outdoor scene in a computer window. Your program can draw 
any outdoor scene that you like as long as it meets these 
requirements:

- The scene must be outdoor and include part of the sky.
- The sky must have clouds.
- The scene must include repetitive objects, such as blades 
of grass, trees, leaves on a tree, birds, flowers, insects, 
fish, pickets in a fence, dashed lines on a road, buildings, 
bales of hay, snowmen, snowflakes, or icicles.

Your program must be divided into functions such as draw_sky, 
draw_cloud, draw_ground, draw_bird, draw_flower, draw_insect, 
draw_fish, or draw_snowman. Each of the objects in your scene 
should be drawn in its own function. To draw the shapes in the 
scene, your program will call functions in a Python library 
named Draw 2-D."""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    
    draw_mountain(canvas, scene_width, scene_height)

    draw_clouds(canvas, 50 , 400, 50)
    draw_clouds(canvas, 125 , 375, 50)
    draw_clouds(canvas, 150 , 400, 50)


    draw_clouds(canvas, 350 , 300, 30)
    draw_clouds(canvas, 365 , 315, 30)
    draw_clouds(canvas, 390 , 300, 30)

    draw_clouds(canvas, 600 , 400, 50)
    draw_clouds(canvas, 530 , 380, 50)
    draw_clouds(canvas, 675 , 415, 50)

    draw_pine_tree(canvas, 510, 0, 300)        
    draw_pine_tree(canvas, 650, 0, 450)

    draw_grass(canvas, scene_width, scene_height, 3)

    draw_bird(canvas, 300, 300)
    draw_bird(canvas, 150, 290)
    draw_bird(canvas, 250, 350)


    
    # draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, width, height):
    draw_rectangle(canvas, 0, 0 , width, height, fill="sky blue")

def draw_mountain(canvas, width, height):
    left = 0
    bottom = 0 
    peak_x = width / 2
    peak_y = height / 1.05
    right = width
    draw_polygon(canvas, left, bottom, peak_x, peak_y, right, bottom, fill="grey")

def draw_clouds(canvas, x, y, diameter):
    draw_oval(canvas, x, y, x + diameter * 3, y + diameter, width=0, fill="white")

def draw_pine_tree(canvas, center_x, bottom, height):
    #Draw trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    top_trunk = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, top_trunk, fill="tan4")

    #Draw skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = top_trunk 
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")

def draw_grass(canvas, width, height, interval):
    #Draw grass
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height * .02, width=2, fill="green2")


def draw_grid(canvas, width, height, interval):
    #Draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    label_x = 15 
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

def draw_bird(canvas, x, y):
    draw_arc(canvas, x-40, y-40, x, y-20, start=0, extent=180, width=5)
    draw_arc(canvas, x, y-40, x+40, y-20, start=0, extent=180, width=5)


# Call the main function so that
# this program will start executing.
main()