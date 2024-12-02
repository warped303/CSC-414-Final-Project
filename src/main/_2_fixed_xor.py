import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def fixed_xor(hex_str1, hex_str2):
    try:
        bytes1 = bytes.fromhex(hex_str1)
        bytes2 = bytes.fromhex(hex_str2)
    except ValueError:
        return "Invalid hex input"

    if len(bytes1) != len(bytes2):
        return "Error: Buffers must be of equal length"

    xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
    return xor_result.hex()


def new_window():
    def solve_challenge2():
        hex_input1 = input_var2a.get()
        hex_input2 = input_var2b.get()
        xor_result = fixed_xor(hex_input1, hex_input2)

        if xor_result:
            solution_var2.set(f"XOR result: {xor_result}")
        else:
            solution_var2.set("Invalid input! Please try again.")

    window = tk.Toplevel()
    window.geometry("800x400")
    window.title("Fixed XOR")

    def load_and_resize_image(image_path, width, height):
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))

    background_image = load_and_resize_image("resources/digitalback.jpg", 800, 400)
    canvas = Canvas(window, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    input_var2a = tk.StringVar()
    input_var2b = tk.StringVar()
    solution_var2 = tk.StringVar()
    solution_var2.set("Your solution will appear here.")

    title_label = tk.Label(window, text='Challenge 2: Fixed XOR', font=("times", 24), bg="#444444", fg="white")
    title_label.place(x=250, y=20)

    input_label1 = tk.Label(window, text='Enter First Hex String:', font=("times", 16), bg="#444444", fg="white")
    input_label1.place(x=100, y=100)

    input_frame1 = Frame(window, bg="#444444", bd=2, relief="groove")
    input_frame1.place(x=100, y=150, width=600, height=50)

    hex_input_1_default = "1c0111001f010100061a024b53535009181c"
    input_entry1 = tk.Entry(input_frame1, textvariable=input_var2a, width=70, font=("times", 14), bg="#333333",
                            fg="white", bd=0)
    input_entry1.pack(fill="both", expand=True)
    input_var2a.set(hex_input_1_default)

    input_label2 = tk.Label(window, text='Enter Second Hex String:', font=("times", 16), bg="#444444", fg="white")
    input_label2.place(x=100, y=210)

    input_frame2 = Frame(window, bg="#444444", bd=2, relief="groove")
    input_frame2.place(x=100, y=260, width=600, height=50)

    hex_input_2_default = "68697420746865206b696420277365792065"
    input_entry2 = tk.Entry(input_frame2, textvariable=input_var2b, width=70, font=("times", 14), bg="#333333",
                            fg="white", bd=0)
    input_entry2.pack(fill="both", expand=True)
    input_var2b.set(hex_input_2_default)

    calculate_button = tk.Button(window, text="Calculate XOR", command=solve_challenge2, font=("times", 14), bg="blue",
                                 fg="white")
    calculate_button.place(x=350, y=320)

    solution_label = tk.Label(window, textvariable=solution_var2, font=("times", 16), bg="#444444", fg="white", width=50,
                              anchor="w")
    solution_label.place(x=100, y=350)
