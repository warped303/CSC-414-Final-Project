import pytest
from src.crypto_challenges import detect_ecb, fetch_ciphertexts_from_url

def test_detect_ecb():
    # Example hex strings with one ECB mode ciphertext:
    ciphertexts = [
        "6c6f...",
        "d4ee...",
        "d4e...d4e...d4e...",  # Repeated block indicating ECB mode
        "a1b2..."
    ]
    result = detect_ecb(ciphertexts)
    assert result is not None
    index, ecb_ciphertext = result
    assert index == 2
    assert ecb_ciphertext == "d4e...d4e...d4e..."


def test_fetch_ciphertexts_from_url(mocker):
    # Mock the requests.get call to test fetch_ciphertexts_from_url without actual HTTP requests
    mock_response = mocker.Mock()
    mock_response.ok = True
    mock_response.text = "6c6f...\nd4ee...\nd4e...d4e...d4e...\na1b2..."
    mocker.patch('requests.get', return_value=mock_response)

    url = "https://example.com/does-not-matter"
    ciphertexts = fetch_ciphertexts_from_url(url)
    assert isinstance(ciphertexts, list)
    assert len(ciphertexts) == 4
