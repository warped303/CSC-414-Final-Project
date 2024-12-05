# tests/test_fixed_xor.py

import pytest
from src.crypto_challenges import fixed_xor

def test_valid_xor():
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = "68697420746865206b696420277365792065"
    expected = "746865206b6964206d73666b742035703879"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_empty_input():
    hex_str1 = ""
    hex_str2 = ""
    expected = "Error: Empty hex input"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_invalid_hex():
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = "invalidhex"
    expected = "Invalid hex input"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_unequal_lengths():
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = "68697420746865206b6964202773657920"
    expected = "Error: Buffers must be of equal length"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_edge_case_empty_string():
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = ""
    expected = "Error: Empty hex input"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_edge_case_short_input():
    hex_str1 = "a3"
    hex_str2 = "ff"
    expected = "5c"
    result = fixed_xor(hex_str1, hex_str2)
    assert result == expected, f"Expected {expected}, but got {result}"
