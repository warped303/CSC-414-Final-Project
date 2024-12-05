# src/crypto_challenges.py

from Crypto.Cipher import AES
import base64
import string
import requests

letter_frequencies = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
    'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
    'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
    'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
    'z': 0.0007836, ' ': 0.1918182
}

def hex_to_base64(hex_string):
    # Check if the string is empty or None
    if not hex_string:
        return None

    # Attempt to convert the hex string to bytes
    try:
        byte_data = bytes.fromhex(hex_string)
    except ValueError:
        return None  # Return None if the string is not valid hex

    # Convert the byte data to base64
    base64_encoded = base64.b64encode(byte_data)
    
    # Decode the base64 bytes to a string and return it
    return base64_encoded.decode('utf-8')


def fixed_xor(hex_str1, hex_str2):
    # Check for empty inputs
    if not hex_str1 or not hex_str2:  
        return "Error: Empty hex input"
    
    try:
        bytes1 = bytes.fromhex(hex_str1)
        bytes2 = bytes.fromhex(hex_str2)
    except ValueError:
        return "Invalid hex input"

    # Check if both hex strings are the same length
    if len(bytes1) != len(bytes2):  
        return "Error: Buffers must be of equal length"

    # Perform the XOR operation byte by byte
    xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))  
    return xor_result.hex()

def single_byte_xor_cipher(encoded_hex):
    # Check for empty input
    if not encoded_hex:
        return None

    # Validate the input hex string
    try:
        encoded_bytes = bytes.fromhex(encoded_hex)
    except ValueError:
        raise ValueError("Input is not a valid hex string")

    def score_text(text):
        return sum(letter_frequencies.get(char, 0) for char in text.lower())

    results = []

    for key in range(256):
        decoded_chars = ''.join(chr(byte ^ key) for byte in encoded_bytes)

        if all(c in string.printable for c in decoded_chars):
            results.append((score_text(decoded_chars), key, decoded_chars))

    results.sort(reverse=True, key=lambda x: x[0])

    return results[0] if results else None



def detect_single_byte_xor_from_url(url):
    """
    Detects single-byte XOR-encrypted strings from lines in a file accessed via a URL.

    Args:
        url (str): The URL to a text file with each line being a hex-encoded string.

    Returns:
        tuple: Best decrypted message and the key used to decrypt it.
    """
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    if not response.text:
        return "", None  # Return empty string and None when content is empty
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



def repeating_key_xor(plaintext, key):
    if not key:
        raise ValueError("Key cannot be empty")
    if not plaintext:  # If the plaintext is empty, return an empty string
        return ""
    
    # Ensure the key is long enough by repeating it to match the length of the plaintext
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    
    # XOR each character of the plaintext with the corresponding character of the key
    xor_result = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    
    # Return the result as a hex-encoded string
    return xor_result.encode().hex()



def decrypt_repeating_key_xor(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypts a ciphertext with a repeating-key XOR encryption."""
    return bytes([c ^ key[i % len(key)] for i, c in enumerate(ciphertext)])



def hamming_distance(str1: bytes, str2: bytes) -> int:
    """Returns the Hamming distance between two byte strings."""
    if len(str1) != len(str2):
        raise ValueError("Inputs must be of equal length")
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))



def aes_ecb_decrypt(url, key):
    # Fetch encrypted data
    response = requests.get(url)
    encrypted_data = base64.b64decode(response.text)
    
    # Decrypt using AES in ECB mode
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(encrypted_data)
    
    # Remove padding (assuming PKCS7 padding)
    pad_len = decrypted_bytes[-1]
    decrypted_bytes = decrypted_bytes[:-pad_len]

    # Decode bytes to string
    decrypted_text = decrypted_bytes.decode('utf-8')
    
    return decrypted_text


def detect_ecb(ciphertexts):
    for idx, hex_ciphertext in enumerate(ciphertexts):
        ciphertext = bytes.fromhex(hex_ciphertext)
        blocks = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
        if len(blocks) != len(set(blocks)):
            return idx, hex_ciphertext
    return None

def fetch_ciphertexts_from_url(url):
    response = requests.get(url)
    if response.ok:
        return response.text.strip().splitlines()
    return None