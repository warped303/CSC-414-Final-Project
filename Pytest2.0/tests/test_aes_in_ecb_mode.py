import pytest
from unittest.mock import patch
from src.crypto_challenges import aes_ecb_decrypt

@patch('requests.get')
def test_aes_ecb_decrypt(mock_get):
    # Valid, padded ciphertext (base64-encoded)
    valid_ciphertext = "CZBDxABQX4FGG/RqvZlyUg9yREaTXnBL0uTj4R5EG0I="  # Adjust if necessary
    mock_get.return_value.text = valid_ciphertext

    # Test inputs
    url = "http://example.com/encrypted"
    key = "YELLOW SUBMARINE"

    # Expected decrypted output
    expected_output = "Decrypted sample text"

    # Execute the decryption function
    result = aes_ecb_decrypt(url, key)

    # Assert the output matches the expected result
    assert result == expected_output, f"Expected: {expected_output}, but got: {result}"


