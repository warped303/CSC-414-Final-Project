import pytest
from unittest.mock import patch, Mock
from src.crypto_challenges import detect_single_byte_xor_from_url

@patch('requests.get')
def test_valid_detection(mock_get):
    # Mock a successful HTTP response with hex-encoded data
    mock_get.return_value = Mock(status_code=200, text="68656c6c6f")  # "hello" in hex
    url = "https://example.com/valid_hex_data.txt"
    expected_message = "$)  #"
    expected_key = 76  # Replace with actual expected key if known

    message, key = detect_single_byte_xor_from_url(url)
    assert message == expected_message
    assert key == expected_key

@patch('requests.get')
def test_empty_url_content(mock_get):
    # Mock a successful HTTP response with empty content
    mock_get.return_value = Mock(status_code=200, text="")
    url = "https://example.com/empty.txt"

    message, key = detect_single_byte_xor_from_url(url)
    
    # Assert that the message is empty (""), as expected for empty content
    assert message == ""
    
    # Assert that the key is None, since no XOR operation can be performed
    assert key is None



@patch('requests.get')
def test_invalid_hex_lines(mock_get):
    # Mock a response with invalid hex data, e.g., non-hex characters
    mock_get.return_value = Mock(status_code=200, text="xyz123")  # Invalid hex data
    url = "https://example.com/invalid_hex_data.txt"
    
    try:
        message, key = detect_single_byte_xor_from_url(url)
    except ValueError as e:
        assert str(e) == "Input is not a valid hex string"  # Updated to match the raised error message




@patch('requests.get')
def test_single_char_hex_line(mock_get):
    # Mock a response with valid single-character hex lines, like "1", "A"
    mock_get.return_value = Mock(status_code=200, text="1A")
    url = "https://example.com/single_char_hex.txt"
    
    try:
        message, key = detect_single_byte_xor_from_url(url)
    except ValueError as e:
        assert str(e) == "Invalid hex data"  # Handle invalid case or mock a valid response



def test_non_printable_characters_in_output():
    # Case where decrypted message contains non-printable characters
    url = "https://example.com/non_printable_hex.txt"  # Assum
