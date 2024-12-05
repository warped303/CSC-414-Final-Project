# CSC-414-Final-Project

## Description

This project is a small software suite designed to solve the first set of [cryptopals crypto challenges](https://cryptopals.com/), with a UI for navigating to and interacting with each challenge. Additionally, a test suite is provided to ensure the correctness of each challenge implementation.

## Installation Instructions

1. Clone the project repository, either by running `git clone https://github.com/warped303/CSC-414-Final-Project.git`  in your terminal / command line if you have Git installed or by clicking on Code -> Download ZIP on the main project page.
2. Make sure you have Python 3 and Pip installed, then run `pip install -r [Path to requirements.txt]` in your terminal / command prompt to install the required Python modules, replacing `[Path to requirements.txt]` with the path to the `requirements.txt` file from the current working directory.
   - If you get an error along the lines of Pip not being installed, try replacing `pip` with `python -m pip`, `python3 -m pip`, or `pip3`.
4. To run the program, run `src/main/main.py` in Python 3.

## Pytest
Use this in console to run Pytest:  
`pytest tests/test_hex_to_base64.py`  
`pytest tests/test_fixed_xor.py`  
`pytest tests/test_single_byte_xor_cipher.py`  
`pytest -v tests/test_detect_single_byte_xor_from_url.py`  
`pytest tests/test_repeating_key_xor.py`  
`pytest tests/test_break_repeating_key_xor.py`  
`pytest tests/test_aes_in_ecb_mode.py`  
`pytest tests/test_detect_aes_in_ecb_mode.py`  

## Credits

- Levi Rawls: Challenge UI implementation
- Stephen Vassalo: Test suite
- David Hovas: Main UI implementation
- Amber McDowell: Challenges 7-8
- Joel Martin: Challenges 4-6
- Sibin Joshi: Challenges 1-3
- Cory Washington: UI layout and design
