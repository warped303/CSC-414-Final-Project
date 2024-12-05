# test_repeating_key_xor.py

import pytest
from src.crypto_challenges import repeating_key_xor

def test_repeating_key_xor():
    # Test with sample inputs
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    
    expected_output = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )
    
    # Call the repeating_key_xor function
    encrypted_text = repeating_key_xor(plaintext, key)
    
    # Assert that the result is as expected
    assert encrypted_text == expected_output

def test_repeating_key_xor_empty_key():
    # Test with an empty key
    plaintext = "Test message"
    key = ""
    
    with pytest.raises(ValueError):
        repeating_key_xor(plaintext, key)

def test_repeating_key_xor_empty_plaintext():
    # Test with an empty plaintext
    plaintext = ""
    key = "KEY"
    
    result = repeating_key_xor(plaintext, key)
    assert result == ""

