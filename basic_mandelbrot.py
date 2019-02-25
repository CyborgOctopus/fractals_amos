import math
import pygame as pg

# Constants
MAX_COLOR = 255

# Global variables
width = 1200
height = 800
display_size = (width, height)
new_aspect_ratio = 1/400
real_offset = -0.5
imag_offset = 0


# Returns complex numbers
def get_complex_number(a, b):
    real = new_aspect_ratio*(a - width/2) + real_offset
    imag = new_aspect_ratio*(b - height/2) + imag_offset
    return complex(real, imag)


# Determines how long a particular point in the complex plane took to escape
def num_iters_to_escape(c, max_iters):
    z = 0
    for i in range(max_iters):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iters


# Returns a color based on how many iterations it took the point to escape
def color(num_iters, max_iters):
    return 0, 0, MAX_COLOR*math.sqrt(num_iters/max_iters)


# Creates the pygame display
def create_screen():
    pg.init()
    screen = pg.display.set_mode(display_size)
    return screen


# Executes the animation loop
def animation_loop():
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


# Displays the mandelbrot set
def display_mandelbrot(max_iters):
    screen = create_screen()
    for i in range(width):
        for j in range(height):
            c = get_complex_number(i, j)
            num_iters = num_iters_to_escape(c, max_iters)
            screen.set_at((i, j), color(num_iters, max_iters))
    animation_loop()


# Allows the user to enter a number of iterations
def get_user_input():
    return int(input("Number of iterations: "))


def main():
    max_iters = get_user_input()
    display_mandelbrot(max_iters)


main()
