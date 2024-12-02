import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import base64


def hex_to_base64(hex_string):
    try:
        byte_data = bytes.fromhex(hex_string)
    except ValueError:
        return None
    base64_encoded = base64.b64encode(byte_data)
    return base64_encoded.decode('utf-8')


def new_window():
    def solve_challenge1():
        hex_input = input_var.get()
        base64_output = hex_to_base64(hex_input)

        if base64_output:
            solution_var.set(f"Base64: {base64_output}")
        else:
            solution_var.set("Invalid hex input! Please try again.")

    window = tk.Toplevel()
    window.geometry("1080x560")
    window.title("Hex to Base64 Converter")

    def load_and_resize_image(image_path, width, height):
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))

    background_image = load_and_resize_image("resources/digitalback.jpg", 1080, 560)
    canvas = Canvas(window, width=1080, height=560)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    input_var = tk.StringVar()
    solution_var = tk.StringVar()
    solution_var.set("Your solution will appear here.")

    title_label = tk.Label(window, text="Challenge 1: Convert Hex to Base64", font=("times", 24), bg="#444444", fg="white")
    title_label.place(x=350, y=20)

    input_label = tk.Label(window, text="Enter Hex String:", font=("times", 16), bg="#444444", fg="white")
    input_label.place(x=100, y=100)

    input_frame = Frame(window, bg="#444444", bd=2, relief="groove")
    input_frame.place(x=100, y=150, width=870, height=50)

    hex_default = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    input_entry = tk.Entry(input_frame, textvariable=input_var, width=72, font=("times", 14), bg="#333333", fg="white", bd=0)
    input_entry.pack(fill="both", expand=True)
    input_var.set(hex_default)

    convert_button = tk.Button(window, text="Convert", command=solve_challenge1, font=("times", 14), bg="blue", fg="white")
    convert_button.place(x=450, y=220)

    solution_label = tk.Label(window, textvariable=solution_var, font=("times", 16), bg="#444444", fg="white", width=70, anchor="w")
    solution_label.place(x=100, y=250)
