import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def repeating_key_xor(plaintext, key):
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    xor_result = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return xor_result.encode().hex()


def load_and_resize_image(image_path, width, height):
    img = Image.open(image_path)
    return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))


def new_window():
    def solve_challenge5():
        plaintext_input_value = input_var5.get()
        key_input_value = key_var5.get()
        try:
            encrypted_text = repeating_key_xor(plaintext_input_value, key_input_value)
            solution_var5.delete(1.0, tk.END)
            solution_var5.insert(tk.END, f"Encrypted: {encrypted_text}")
        except ValueError as e:
            solution_var5.delete(1.0, tk.END)
            solution_var5.insert(tk.END, f"Invalid input! {str(e)}")

    window = tk.Toplevel()
    window.geometry("1000x600")
    window.title("5. Repeating Key XOR")

    background_image = load_and_resize_image("resources/digitalback.jpg", 1000, 600)
    canvas = Canvas(window, width=1000, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    global input_var5, key_var5, solution_var5
    input_var5 = tk.StringVar()
    key_var5 = tk.StringVar()
    solution_var5 = tk.Text(window, height=5, width=80, font=("times", 14), bg="#333333", fg="white", bd=0)
    solution_var5.insert(tk.END, "Your solution will appear here.")

    title_label = tk.Label(window, text='Challenge 5: Repeating-key XOR', font=("times", 24), bg="#444444", fg="white")
    title_label.place(x=300, y=20)

    plaintext_label = tk.Label(window, text='Enter Plaintext:', font=("times", 16), bg="#444444", fg="white")
    plaintext_label.place(x=100, y=100)

    plaintext_frame = Frame(window, bg="#444444", bd=2, relief="groove")
    plaintext_frame.place(x=100, y=150, width=800, height=50)

    plaintext_input_default = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    plaintext_input = tk.Entry(plaintext_frame, textvariable=input_var5, width=70, font=("times", 14), bg="#333333",
                               fg="white", bd=0)
    plaintext_input.pack(fill="both", expand=True)
    input_var5.set(plaintext_input_default)

    key_label = tk.Label(window, text='Enter Key:', font=("times", 16), bg="#444444", fg="white")
    key_label.place(x=100, y=210)

    key_frame = Frame(window, bg="#444444", bd=2, relief="groove")
    key_frame.place(x=100, y=260, width=800, height=50)

    key_input_default = "ICE"
    key_input = tk.Entry(key_frame, textvariable=key_var5, width=70, font=("times", 14), bg="#333333",
                         fg="white", bd=0)
    key_input.pack(fill="both", expand=True)
    key_var5.set(key_input_default)

    encrypt_button = tk.Button(window, text="Encrypt", command=solve_challenge5, font=("times", 14), bg="blue", fg="white")
    encrypt_button.place(x=400, y=320)

    solution_label = tk.Label(window, text='Encrypted Output:', font=("times", 16), bg="#444444", fg="white")
    solution_label.place(x=100, y=380)

    solution_var5.place(x=100, y=410, width=800, height=100)
