import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # for image resizing only. (PIP Install Pillow)
import os

import _1_hex_to_base64 as ch1
import _2_fixed_xor as ch2
import _3_single_byte_xor_cipher as ch3
import _4_detect_single_character_xor as ch4
import _5_repeating_key_xor as ch5
import _6_break_repeating_key_xor as ch6
import _7_aes_in_ecb_mode as ch7
import _8_detect_aes_in_ecb_mode as ch8


def challenge1():
    ch1.new_window()


def challenge2():
    ch2.new_window()


def challenge3():
    ch3.new_window()


def challenge4():
    ch4.new_window()


def challenge5():
    ch5.new_window()


def challenge6():
    ch6.new_window()


def challenge7():
    ch7.new_window()


def challenge8():
    ch8.new_window()


def main():
    # Create the main window
    root = tk.Tk(className='Cryptopals Challenges Set 1')
    root.geometry("1080x560")
    root.title("Crypto Paycheck")

    # Create a label widget
    label = tk.Label(root,
                     text='Cryptopals Challenges Set 1',
                     width="25",
                     anchor="center",
                     font="times")
    label.pack()

    def load_and_resize_image(image_path, width, height):
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))

    original_image = Image.open("resources/code.png")

    challenge1_image = load_and_resize_image("resources/CHTTB64.png", 480, 60)
    challenge2_image = load_and_resize_image("resources/FXOR.png", 480, 60)
    challenge3_image = load_and_resize_image("resources/SBXORC.png", 480, 60)
    challenge4_image = load_and_resize_image("resources/DSCXOR.png", 480, 60)
    challenge5_image = load_and_resize_image("resources/IRKXOR.png", 480, 60)
    challenge6_image = load_and_resize_image("resources/BRKXOR.png", 480, 60, )
    challenge7_image = load_and_resize_image("resources/AIEM.png", 480, 60)
    challenge8_image = load_and_resize_image("resources/DAIEM.png", 480, 60)
    resized_image = original_image.resize((1080, 560), Image.LANCZOS)

    # adds converted image

    bg = ImageTk.PhotoImage(resized_image)

    image_width = bg.width()
    image_height = bg.height()

    # creates canvas/backgound
    canvas1 = Canvas(root,
                     width=1080,
                     height=560)

    canvas1.pack(fill="both",
                 expand=True)

    x = (1080 - image_width) // 2
    y = (560 - image_height) // 2

    canvas1.create_image(x, y, image=bg,
                         anchor="nw",
                         )

    # creates buttons to click
    challenge1Button = tk.Button(root,
                                 image=challenge1_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge1)
    challenge1Button.place(x=50, y=200)

    challenge2Button = tk.Button(root,
                                 image=challenge2_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge2)
    challenge2Button.place(x=580, y=200)

    challenge3Button = tk.Button(root,
                                 image=challenge3_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge3)
    challenge3Button.place(x=50, y=300)

    challenge4Button = tk.Button(root,
                                 image=challenge4_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge4)
    challenge4Button.place(x=580, y=300)

    challenge5Button = tk.Button(root,
                                 image=challenge5_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge5)
    challenge5Button.place(x=50, y=398)

    challenge6Button = tk.Button(root,
                                 image=challenge6_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge6)
    challenge6Button.place(x=580, y=395)

    challenge7Button = tk.Button(root,
                                 image=challenge7_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge7)
    challenge7Button.place(x=50, y=490)

    challenge8Button = tk.Button(root,
                                 image=challenge8_image,
                                 compound="none",
                                 overrelief="groove",
                                 command=challenge8)
    challenge8Button.place(x=580, y=490)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
