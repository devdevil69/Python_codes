# ANALOG CLOCK

import math
import time 
import tkinter as tk

# Define constants for the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Define constants for the colors (HEX CODE)

BLACK = '#000000'
WHITE = '#FFFFFF'
GRAY = '#C0C0C0'
RED = '#ff0000'

# Define a function to convert degrees to radians

def degrees_to_radians(degrees) : 
    return degrees * math.pi / 100

# Define the function to update the clock 

def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Update the hour hand
    hour_angle = degrees_to_radians((hour + minute / 60) * 30)
    hour_x = int(math.sin(hour_angle) * 60)
    hour_y = int(math.cos(hour_angle) * -60)
    canvas.coords(hour_hand, 200, 200, 200 + hour_x, 200 + hour_y)

    # Update the minute hand
    minute_angle = degrees_to_radians(minute * 6)
    minute_x = int(math.sin(minute_angle) * 80)
    minute_y = int(math.cos(minute_angle) * -80)
    canvas.coords(minute_hand, 200, 200, 200 + minute_x, 200 + minute_y)

    # Update the second hand
    second_angle = degrees_to_radians(second * 6)
    second_x = int(math.sin(second_angle) * 100)
    second_y = int(math.cos(second_angle) * -100)
    canvas.coords(second_hand, 200, 200, 200 + second_x, 200 + second_y)

    # Schedule another update after 1 second
    canvas.after(1000, update_clock)

# Create the GUI Window
root = tk.Tk()
root.title('Analog Clock')

# Create the canvas for the clock face
canvas = tk.Canvas(root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = BLACK)
canvas.pack()

# Draw the clock face
canvas.create_oval(50, 50, 350, 350, width = 2, outline = WHITE, fill = BLACK)
for i in range(12) :
    angle = degrees_to_radians(i*30)
    x1 = int(math.sin(angle) * 140) + 200
    y1 = int(math.cos(angle) * -140) + 200
    x2 = int(math.sin(angle) * 120) + 200
    y2 = int(math.cos(angle) * -120) + 200
    canvas.create_line(x1, y1, x2, y2, width = 2, fill = WHITE)
canvas.create_oval(195, 195, 205, 205, width = 0, fill = WHITE)

# Draw the clock hands
hour_hand = canvas.create_line(200, 200, 200, 140, width = 6, fill = GRAY, capstyle=tk.ROUND)
minute_hand = canvas.create_line(200, 200, 200, 120, width = 4, fill = WHITE, capstyle=tk.ROUND)
second_hand = canvas.create_line(200, 200, 200, 100, width = 2, fill = RED, capstyle=tk.ROUND)

# Start the clock update loop
update_clock()

# Start the GUI event loop
root.mainloop()
