# tests/test_hex_to_base64.py
import sys
from pathlib import Path

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from src.crypto_challenges import hex_to_base64

def test_valid_hex():
    # Testing a valid hex input that should produce a specific base64 output
    input_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    result = hex_to_base64(input_hex)
    assert result == expected_base64, f"Expected {expected_base64}, but got {result}"

def test_invalid_hex():
    # Testing an invalid hex input, which should return None
    input_hex = "InvalidHexString"
    result = hex_to_base64(input_hex)
    assert result is None, f"Expected None, but got {result}"

def test_empty_hex():
    # Testing an empty hex string, which should ideally return None
    input_hex = ""
    result = hex_to_base64(input_hex)
    assert result is None, f"Expected None, but got {result}"

def test_short_valid_hex():
    # Testing a very short valid hex string
    input_hex = "a3"
    expected_base64 = "ow=="
    result = hex_to_base64(input_hex)
    assert result == expected_base64, f"Expected {expected_base64}, but got {result}"

def test_empty_string():
    # Testing an empty string input, which should return None
    input_hex = ""
    result = hex_to_base64(input_hex)
    assert result is None, f"Expected None, but got {result}"

def test_invalid_character_hex():
    # Testing a hex string with non-hex characters
    input_hex = "ZZZ"
    result = hex_to_base64(input_hex)
    assert result is None, f"Expected None, but got {result}"
