import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests
from _3_single_byte_xor_cipher import single_byte_xor_cipher


def detect_single_byte_xor_from_url(url):
    response = requests.get(url)
    lines = response.text.splitlines()

    best_score = None
    best_decrypted_message = None
    best_key = None

    for line in lines:
        result = single_byte_xor_cipher(line)
        if result is not None:
            score, key, decrypted_message = result
            if best_score is None or score > best_score:
                best_score = score
                best_key = key
                best_decrypted_message = decrypted_message

    return best_decrypted_message, best_key


def load_and_resize_image(image_path, width, height):
    img = Image.open(image_path)
    return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))


def new_window():
    def print_output():
        url = url_input.get()
        message, key = detect_single_byte_xor_from_url(url)
        best_decrypted_message_string.set("Best decrypted message: " + message)
        key_used_string.set("Using key: " + str(key))

    window = tk.Toplevel()
    window.geometry("800x400")
    window.title("4. Detect Single Character XOR")

    background_image = load_and_resize_image("resources/digitalback.jpg", 800, 400)
    canvas = Canvas(window, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    input_label_string = tk.StringVar()
    input_label_string.set("Input URL to hex encoded string (https://example.com/example.txt)")

    title_label = tk.Label(window, text='Challenge 4: Detect Single Character XOR', font=("times", 24), bg="#444444",
                           fg="white")
    title_label.place(x=200, y=20)

    input_label = tk.Label(window, textvariable=input_label_string, font=("times", 16), bg="#444444", fg="white")
    input_label.place(x=100, y=100)

    url_input_default = "https://cryptopals.com/static/challenge-data/4.txt"

    input_frame = Frame(window, bg="#444444", bd=2, relief="groove")
    input_frame.place(x=100, y=150, width=600, height=50)

    url_input = tk.Entry(input_frame, width=70, font=("times", 14), bg="#333333", fg="white", bd=0)
    url_input.pack(fill="both", expand=True)
    url_input.insert(0, url_input_default)

    print_button = tk.Button(window, text="Detect from URL", command=print_output, font=("times", 14), bg="blue",
                             fg="white")
    print_button.place(x=350, y=220)

    best_decrypted_message_string = tk.StringVar()
    best_decrypted_message_string.set("Best decrypted message: ")

    best_decrypted_message_label = tk.Label(window, textvariable=best_decrypted_message_string, font=("times", 16),
                                            bg="#444444", fg="white", width=70, anchor="w")
    best_decrypted_message_label.place(x=100, y=280, width=600)

    key_used_string = tk.StringVar()
    key_used_string.set("Using key: ")

    key_used_label = tk.Label(window, textvariable=key_used_string, font=("times", 16), bg="#444444", fg="white",
                              width=70, anchor="w")
    key_used_label.place(x=100, y=320, width=600)
