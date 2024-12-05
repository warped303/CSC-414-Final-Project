import pytest
from src.crypto_challenges import decrypt_repeating_key_xor, hamming_distance


# Test for Hamming distance function
def test_hamming_distance():
    # Test data for Hamming distance
    str1 = b'this is a test'
    str2 = b'wokka wokka!!!'

    # Expected Hamming distance
    expected_distance = 37
    result = hamming_distance(str1, str2)  # Use Hamming distance function, not decrypt
    assert result == expected_distance


# Test for decrypt_repeating_key_xor with ciphertext and key
def test_decrypt_repeating_key_xor():
    # Sample ciphertext and key
    ciphertext = b'Example ciphertext to test repeating-key XOR decryption.'
    key = b'X'  # Correct key for testing

    # Expected decrypted message
    expected_decrypted_message = b'\x1d 95(4=x;1(0=*,= ,x,7x,=+,x*=(=9,16?u3=!x\x00\x17\nx<=;*!(,176v'


    # Decrypt using repeating-key XOR
    result = decrypt_repeating_key_xor(ciphertext, key)

    assert result == expected_decrypted_message, f"Expected {expected_decrypted_message}, but got {result}"
