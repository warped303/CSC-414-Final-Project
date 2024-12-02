import tkinter as tk
import requests


def detect_ecb(ciphertexts):
    for idx, hex_ciphertext in enumerate(ciphertexts):
        ciphertext = bytes.fromhex(hex_ciphertext)
        blocks = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
        if len(blocks) != len(set(blocks)):
            return idx, hex_ciphertext
    return None


def new_window():
    def print_output():
        url = url_input.get()
        response = requests.get(url)
        ciphertexts = response.text.strip().splitlines()
        result = detect_ecb(ciphertexts)

        ECB_ciphertext_text.delete("1.0", "end")
        if result:
            index, ecb_ciphertext = result
            ECB_ciphertext_text.insert(tk.END, f"ECB-encrypted ciphertext found at line {index + 1}: {ecb_ciphertext}")
        else:
            ECB_ciphertext_text.insert(tk.END, "No ECB-encrypted ciphertext found.")


    def solve_challenge8():
        hex_input = input_var8.get()
        try:
            result = detect_ecb([hex_input])
            if result:
                index, ecb_ciphertext = result
                solution_var8.set(f"ECB ciphertext found at line {index + 1}: {ecb_ciphertext}")
            else:
                solution_var8.set("No ECB ciphertext found.")
        except ValueError:
            solution_var8.set("Invalid hex input!")


    def challenge8_ui():
        challenge8_window = tk.Toplevel()
        challenge8_window.title("Challenge 8: Detect AES in ECB Mode")

        global input_var8, solution_var8
        input_var8 = tk.StringVar()
        solution_var8 = tk.StringVar()
        solution_var8.set("Your solution will appear here.")

        label = tk.Label(challenge8_window, text='Challenge 8: Detect AES in ECB Mode', font=("times", 14),
                         bg="#444444",
                         fg="white")
        label.pack(pady=10)

        input_label = tk.Label(challenge8_window, text='Enter Ciphertext (Hex):', font=("times", 12), bg="#444444",
                               fg="white")
        input_label.pack(pady=5)

        input_entry = tk.Entry(challenge8_window, textvariable=input_var8, font=("times", 12), bg="#333333", fg="white",
                               width=50)
        input_entry.pack(pady=5)

        submit_button = tk.Button(challenge8_window, text='Detect', command=solve_challenge8, font=("times", 14),
                                  bg="blue",
                                  fg="white")
        submit_button.pack(pady=10)

        solution_label = tk.Label(challenge8_window, textvariable=solution_var8, font=("times", 12), bg="#444444",
                                  fg="white")
        solution_label.pack(pady=5)

    window = tk.Toplevel()
    window.geometry("800x600")
    window.title("8. Detect AES in ECB mode")


    background_image = tk.PhotoImage(file="resources/digitalback.jpg")
    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

    title_label = tk.Label(window,
                            text="Challenge 8: Detect AES in ECB mode",
                            font=("times", 16), bg="#444444", fg="white")
    title_label.pack(pady=20)

    input_label_string = tk.StringVar()
    input_label_string.set("Input URL with ECB ciphertext (https://example.com/example.txt)")
    input_label = tk.Label(window, textvariable=input_label_string, font=("times", 14), bg="#444444", fg="white")
    input_label.pack(pady=20)

    url_input_default = "https://cryptopals.com/static/challenge-data/8.txt"
    url_input = tk.Entry(window, width=len(url_input_default) + 10, font=("times", 12), bg="#333333", fg="white")
    url_input.pack(pady=5)
    url_input.insert(0, url_input_default)

    print_button = tk.Button(window, text="Print Output", command=print_output, font=("times", 14), bg="blue", fg="white")
    print_button.pack(pady=20)

    ECB_ciphertext_label_string = tk.StringVar()
    ECB_ciphertext_label_string.set("ECB ciphertext:")
    ECB_ciphertext_label = tk.Label(window, textvariable=ECB_ciphertext_label_string, font=("times", 14), bg="#444444",
                                    fg="white")
    ECB_ciphertext_label.pack(pady=5)

    ECB_ciphertext_text = tk.Text(window, width=64, height=10, font=("times", 12), bg="#333333", fg="white")
    ECB_ciphertext_text.pack(pady=5)
