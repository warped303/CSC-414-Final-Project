import tkinter as tk
from Crypto.Cipher import AES
import base64
import requests
from PIL import Image, ImageTk


def load_and_resize_image(image_path, width, height):
    img = Image.open(image_path)
    return ImageTk.PhotoImage(img.resize((width, height), Image.LANCZOS))


def aes_ecb_decrypt(url, key):
    response = requests.get(url)
    ciphertext = base64.b64decode(response.text)

    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode('utf-8')


def new_window():
    def print_output():
        url = url_input.get()
        key = key_input.get()
        try:
            decrypted_message = aes_ecb_decrypt(url, key)
            message_text.delete("1.0", "end")
            message_text.insert(tk.END, decrypted_message)
        except Exception as e:
            message_text.delete("1.0", "end")
            message_text.insert(tk.END, str(e))

    window = tk.Toplevel()
    window.geometry("800x600")
    window.title("7. AES in ECB mode")

    background_image = load_and_resize_image("resources/digitalback.jpg", 800, 600)
    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

    title_label = tk.Label(window,
                            text="Challenge 7: AES in ECB mode",
                            font=("times", 16), bg="#444444", fg="white")
    title_label.pack(pady=10)

    input_label_string = tk.StringVar()
    input_label_string.set("Input URL to Base64 text and key")
    input_label = tk.Label(window,
                           textvariable=input_label_string,
                           font=("times", 14), bg="#444444", fg="white")
    input_label.pack(pady=10)

    url_input_default = "https://cryptopals.com/static/challenge-data/7.txt"
    url_input = tk.Entry(window,
                         width=len(url_input_default)+10, font=("times", 12), bg="#333333", fg="white")
    url_input.pack(pady=5)
    url_input.insert(0, url_input_default)

    key_input_default = "YELLOW SUBMARINE"
    key_input = tk.Entry(window,
                         width=len(key_input_default)+5, font=("times", 12), bg="#333333", fg="white")
    key_input.pack(pady=5)
    key_input.insert(0, key_input_default)

    print_button = tk.Button(window,
                             text="Decrypt",
                             command=print_output,
                             font=("times", 14), bg="blue", fg="white")
    print_button.pack(pady=20)

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
