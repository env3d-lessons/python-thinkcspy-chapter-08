import image
import random

"""
The following function is simply an example of how to create a new image
using the image library from the text.  Here we create an image
of width and height and set every pixel to red using a nested loop
as outline in chatper 8.11

"""
def createRedImage(width, height):

    im = image.EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            im.setPixel(x, y, image.Pixel(255, 0, 0))

    return im


"""
Exercise 1

Create a image called white_line.gif where the entire image
is black with a single white line across the middle of the image

"""
def createWhiteLine(width, height):
    im = image.EmptyImage(width, height)
    mid_y = height // 2
    for x in range(width):
        for y in range(height):
            if y == mid_y:
                im.setPixel(x, y, image.Pixel(255, 255, 255))  # White
            else:
                im.setPixel(x, y, image.Pixel(0, 0, 0))        # Black
    return im

"""
Exercise 2

Create an image called alternate_lines.gif where we have horizontal lines 
that alternate between black and white
"""
def createAlternateLines(width, height):
    im = image.EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            if y % 2 == 0:
                im.setPixel(x, y, image.Pixel(255, 255, 255))  # White
            else:
                im.setPixel(x, y, image.Pixel(0, 0, 0))        # Black
    return im

"""
Exercise 3

Using the random.random() function, create an image called random.gif where
each pixel has a 50% chance of being white or black
"""
def createRandomNoise(width, height):
    im = image.EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            if random.random() < 0.5:
                im.setPixel(x, y, image.Pixel(255, 255, 255))  # White
            else:
                im.setPixel(x, y, image.Pixel(0, 0, 0))        # Black
    return im

"""
Exercise 4

Steganography is the practice of concealing a file, message, image, or video within another 
file, message, image, or video. 

The file encoded_image.gif looks normal, but we actually hid a secret black and white
image inside the red channel.  Implement the following algorithm:

 - The secret image is the same width and size of encoded.gif
 - Use our nested loop to process each pixel:
     - If the red channel is odd, turn the resulting pixel on the new image to black
     - if the red channel is even, turn the resulting pixel on the new image to red

"""
def decodeImage():
    secret = image.Image("encoded.png")    
    for x in range(secret.width):
        for y in range(secret.height):
            pix = secret.getPixel(x, y)
            if pix.getRed() % 2 == 1:
                secret.setPixel(x, y, image.Pixel(0, 0, 0))        # Black
            else:
                secret.setPixel(x, y, image.Pixel(255, 0, 0))      # Red
    return secret


### GUI Code - DO NOT MODIFY ####

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk  # Requires pillow

class ImageGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Generator")

        self.width = 728
        self.height = 410
        
        # Use a frame to hold canvas and buttons side by side
        main_frame = tk.Frame(master)
        main_frame.pack(pady=10)

        # Canvas on the left
        self.canvas = tk.Canvas(main_frame, bg="gray", width=self.width, height=self.height)
        self.canvas.pack(side=tk.LEFT, padx=10)

        # Buttons in a vertical frame on the right
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

        tk.Button(btn_frame, text="Create Red Image", width=20, command=self.show_red).pack(pady=5)
        tk.Button(btn_frame, text="Create White Line", width=20, command=self.show_white_line).pack(pady=5)
        tk.Button(btn_frame, text="Create Alternate Lines", width=20, command=self.show_alternate_lines).pack(pady=5)
        tk.Button(btn_frame, text="Create Random Noise", width=20, command=self.show_random_noise).pack(pady=5)
        tk.Button(btn_frame, text="Decode Image", width=20, command=self.show_decoded).pack(pady=5)

        self.tk_img = None  # Keep reference to avoid garbage collection

    def display_image(self, im):
        from PIL import ImageTk
        pil_img = im.im  # This should be a PIL Image
        self.tk_img = ImageTk.PhotoImage(pil_img, master=self.master)  # Explicitly set master
        self.canvas.delete("all")
        self.id = self.canvas.create_image(0, 0, image=self.tk_img, anchor=tk.NW)

    def show_red(self):
        im = createRedImage(self.width, self.height)
        self.display_image(im)

    def show_white_line(self):
        im = createWhiteLine(self.width, self.height)
        self.display_image(im)

    def show_alternate_lines(self):
        im = createAlternateLines(self.width, self.height)
        self.display_image(im)

    def show_random_noise(self):
        im = createRandomNoise(self.width, self.height)
        self.display_image(im)

    def show_decoded(self):
        im = decodeImage()
        self.display_image(im)

def main_gui():

    root = tk.Tk()
    app = ImageGUI(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Ensure exit on close
    root.mainloop()

if __name__ == "__main__":
    main_gui()
