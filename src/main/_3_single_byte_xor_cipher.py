import tkinter as tk
import string
from tkinter import Frame, Canvas
from PIL import Image, ImageTk

letter_frequencies = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
    'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
    'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
    'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
    'z': 0.0007836, ' ': 0.1918182
}

def single_byte_xor_cipher(encoded_hex):
    encoded_bytes = bytes.fromhex(encoded_hex)

    def score_text(text):

        return sum(letter_frequencies.get(char, 0) for char in text.lower())

    results = []

    for key in range(256):

        decoded_chars = ''.join(chr(byte ^ key) for byte in encoded_bytes)

        if all(c in string.printable for c in decoded_chars):

            results.append((score_text(decoded_chars), key, decoded_chars))

    results.sort(reverse=True, key=lambda x: x[0])

    return results[0] if results else None


def new_window():
    def print_output():
        hex_encoded_string = hex_encoded_string_input.get()
        best_score, key_used, decrypted_message = single_byte_xor_cipher(hex_encoded_string)
        best_decrypted_message_string.set("Best decrypted message: " + decrypted_message)
        key_used_string.set("Using key: " + str(key_used))

    window = tk.Toplevel()
    window.geometry("800x400")
    window.title("3. Single Byte XOR Cipher")

    def load_and_resize_image(image_path, width, height):
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))

    background_image = load_and_resize_image("resources/digitalback.jpg", 800, 400)
    canvas = Canvas(window, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    title_label = tk.Label(window, text='Challenge 3: Single Byte XOR Cipher', font=("times", 24), bg="#444444", fg="white")
    title_label.place(x=150, y=20)

    input_label_string = tk.StringVar()
    input_label_string.set("Input hex encoded string (0-9, A-F)")
    input_label = tk.Label(window, textvariable=input_label_string, font=("times", 16), bg="#444444", fg="white")
    input_label.place(x=100, y=100)

    input_frame = Frame(window, bg="#444444", bd=2, relief="groove")
    input_frame.place(x=100, y=150, width=600, height=50)

    hex_encoded_string_input_default = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    hex_encoded_string_input = tk.Entry(input_frame, width=70, font=("times", 14), bg="#333333",
                                         fg="white", bd=0)
    hex_encoded_string_input.pack(fill="both", expand=True)
    hex_encoded_string_input.insert(0, hex_encoded_string_input_default)

    print_button = tk.Button(window, text="Print Output", command=print_output, font=("times", 14), bg="blue", fg="white")
    print_button.place(x=350, y=220)

    best_decrypted_message_string = tk.StringVar()
    best_decrypted_message_string.set("Best decrypted message: ")
    best_decrypted_message_label = tk.Label(window, textvariable=best_decrypted_message_string, font=("times", 16), bg="#444444", fg="white", anchor="w")
    best_decrypted_message_label.place(x=100, y=300)

    key_used_string = tk.StringVar()
    key_used_string.set("Using key: ")
    key_used_label = tk.Label(window, textvariable=key_used_string, font=("times", 16), bg="#444444", fg="white", anchor="w")
    key_used_label.place(x=100, y=350)
