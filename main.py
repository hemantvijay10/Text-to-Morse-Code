"""
Text to Morse Code Converter

Author: Hemant Vijay
Last Updated: 4-Nov-2025

Project Credit:
This project is part of the "100 Days of Code - The Complete Python Pro Bootcamp"
course by Angela Yu on Udemy.
Course Link: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

Description:
This program converts plain text into Morse code. Each letter, number, and common
punctuation mark is translated into its corresponding Morse code representation
using dots and slashes.
"""

# Dictionary that maps each character to its Morse code equivalent
# Dots represent short signals, dashes represent long signals
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def text_to_morse(text):
    """
    Converts a text string into Morse code.

    This function takes any text input and converts each character into its
    Morse code equivalent. Letters are converted to uppercase before translation.
    Characters not in the dictionary are skipped.

    Parameters:
    text (str): The text string to be converted to Morse code

    Returns:
    str: The Morse code representation of the input text, with spaces between each code
    """
    # Convert the input text to uppercase so we can match it with our dictionary
    text = text.upper()

    # Create an empty list to store the Morse code for each character
    morse_code = []

    # Go through each character in the text one by one
    for char in text:
        # Check if the character exists in our Morse code dictionary
        if char in MORSE_CODE_DICT:
            # Add the corresponding Morse code to our list
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # If the character is not in our dictionary, skip it
            # This handles special characters we haven't defined
            continue

    # Join all the Morse codes together with a space between each one
    # This makes it easier to read the final output
    return ' '.join(morse_code)


def main():
    """
    Main function that runs the text to Morse code converter program.

    This function displays a welcome message, asks the user to enter text,
    converts that text to Morse code, and displays the result.
    """
    # Display the program title
    print("=" * 50)
    print("TEXT TO MORSE CODE CONVERTER")
    print("=" * 50)
    print()

    # Ask the user to type the text they want to convert
    user_input = input("Enter the text you want to convert to Morse code: ")

    # Convert the user's text to Morse code using our function
    morse_result = text_to_morse(user_input)

    # Display the converted Morse code to the user
    print()
    print("Morse Code:")
    print(morse_result)
    print()
    print("=" * 50)


# This checks if the program is being run directly (not imported as a module)
# If it is being run directly, it starts the main function
if __name__ == "__main__":
    main()
