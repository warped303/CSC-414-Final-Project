import tkinter as tk
import base64
import requests
from PIL import Image, ImageTk
from _3_single_byte_xor_cipher import letter_frequencies


def hamming_distance(str1, str2):
    assert len(str1) == len(str2)
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))


def repeating_key_xor_decrypt(ciphertext, key):
    return bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])


def score_text(text):
    return sum(letter_frequencies.get(chr(byte).lower(), 0) for byte in text)


def single_byte_xor_cipher(encoded_bytes):
    best_score = None
    best_key = None
    for key in range(256):
        decoded = bytes([b ^ key for b in encoded_bytes])
        score = score_text(decoded)
        if best_score is None or score > best_score:
            best_score = score
            best_key = key
    return best_key


def transpose_blocks(blocks, keysize):
    transposed = [[] for _ in range(keysize)]
    for i, byte in enumerate(blocks):
        transposed[i % keysize].append(byte)
    return [bytes(block) for block in transposed]


def break_repeating_key_xor(ciphertext, keysize):
    blocks = transpose_blocks(ciphertext, keysize)
    key = bytes([single_byte_xor_cipher(block) for block in blocks])
    decrypted_message = repeating_key_xor_decrypt(ciphertext, key)
    return key, decrypted_message


def load_and_resize_image(image_path, width, height):
    img = Image.open(image_path)
    return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))


def new_window():
    def print_output():
        url = url_input.get()
        response = requests.get(url)
        ciphertext = base64.b64decode(response.text)

        keysize = int(keysize_input.get())

        key, message = break_repeating_key_xor(ciphertext, keysize)
        key_string.set("Best Key: " + key.decode())
        message_text.delete("1.0", "end")
        message_text.insert(tk.END, message)

    window = tk.Toplevel()
    window.geometry("800x400")
    window.title("6. Break Repeating Key XOR")

    background_image = load_and_resize_image("resources/digitalback.jpg", 800, 400)
    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

    title_label = tk.Label(window,
                           text="Challenge 6: Break repeating-key XOR",
                           font=("times", 16), bg="#444444", fg="white")
    title_label.pack(pady=10)

    input_label_string = tk.StringVar()
    input_label_string.set("Input URL to Base64 text and keysize")
    input_label = tk.Label(window,
                           textvariable=input_label_string,
                           font=("times", 14), bg="#444444", fg="white")
    input_label.pack(pady=10)

    url_input_default = "https://cryptopals.com/static/challenge-data/6.txt"
    url_input = tk.Entry(window,
                         width=len(url_input_default) + 10, font=("times", 12), bg="#333333", fg="white")
    url_input.pack(pady=5)
    url_input.insert(0, url_input_default)

    keysize_input_default = "29"
    keysize_input = tk.Entry(window,
                             width=4, font=("times", 12), bg="#333333", fg="white")
    keysize_input.pack(pady=5)
    keysize_input.insert(0, keysize_input_default)

    print_button = tk.Button(window,
                             text="Decrypt",
                             command=print_output,
                             font=("times", 14), bg="blue", fg="white")
    print_button.pack(pady=20)

    key_string = tk.StringVar()
    key_string.set("Best Key: ")
    key_label = tk.Label(window,
                         textvariable=key_string,
                         font=("times", 14), bg="#444444", fg="white")
    key_label.pack(pady=5)

    message_label_string = tk.StringVar()
    message_label_string.set("Decrypted message:")
    message_label = tk.Label(window,
                             textvariable=message_label_string,
                             font=("times", 14), bg="#444444", fg="white")
    message_label.pack(pady=5)

    message_frame = tk.Frame(window, bg="#444444")
    message_frame.pack(pady=5)

    message_scrollbar = tk.Scrollbar(message_frame, orient="vertical", bg="#555555")
    message_scrollbar.pack(side=tk.LEFT, fill="y")

    message_text = tk.Text(message_frame,
                           width=80,
                           height=10,
                           yscrollcommand=message_scrollbar.set,
                           font=("times", 12), bg="#333333", fg="white")
    message_text.pack()

    message_scrollbar.config(command=message_text.yview)
