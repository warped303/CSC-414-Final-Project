import pytest
import string
from src.crypto_challenges import single_byte_xor_cipher

def test_valid_single_byte_xor():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    expected_message = "Cooking MC's like a pound of bacon"  # Focus on the decrypted message
    result = single_byte_xor_cipher(hex_str)
    
    # Ensure the decrypted message matches the expected message
    assert result[2] == expected_message, f"Expected message: {expected_message}, but got {result[2]}"


def test_empty_input():
    hex_str = ""
    result = single_byte_xor_cipher(hex_str)
    assert result is None, f"Expected None for empty input, but got {result}"

def test_invalid_hex_input():
    hex_str = "xyz"
    try:
        result = single_byte_xor_cipher(hex_str)
        assert False, "Expected ValueError for invalid hex input, but function did not raise it"
    except ValueError as e:
        assert str(e) == "Input is not a valid hex string", f"Expected error message 'Input is not a valid hex string', but got {str(e)}"

def test_single_char_input():
    hex_str = "1"  # XOR cipher on a single character
    try:
        result = single_byte_xor_cipher(hex_str)
        assert False, "Expected ValueError for invalid hex input, but function did not raise it"
    except ValueError as e:
        assert str(e) == "Input is not a valid hex string", f"Expected error message 'Input is not a valid hex string', but got {str(e)}"


def test_non_printable_characters():
    hex_str = "1b37373331363f78151b7f2b783431333d"
    result = single_byte_xor_cipher(hex_str)
    assert result is not None, f"Expected a result, but got None"
    assert all(c in string.printable for c in result[2]), "Decrypted message contains non-printable characters"

def test_large_input():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b37361b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"  # Large repeated hex string
    result = single_byte_xor_cipher(hex_str)
    assert result is not None, f"Expected a valid result, but got None"

