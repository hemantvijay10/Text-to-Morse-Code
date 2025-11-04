# Text to Morse Code Converter

Author: Hemant Vijay
Last Updated: 4 November 2025

## Project Credit

This project is part of an assignment for the 100 Days of Code course by Angela Yu on Udemy.

Course Link: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

## Overview

This is a simple Python program that converts regular text into Morse code. Morse code is a method of communication that uses dots and dashes to represent letters, numbers, and punctuation marks. This system was historically used for long distance communication via telegraph and radio.

## What This Program Does

The program takes any text you type and converts each letter, number, and common punctuation mark into its Morse code equivalent. For example, the letter A becomes dot dash, the letter B becomes dash dot dot dot, and so on.

## How to Use

1. Make sure you have Python installed on your computer.
2. Open a terminal or command prompt.
3. Navigate to the folder containing main.py.
4. Run the program by typing: python main.py
5. When prompted, enter the text you want to convert.
6. The program will display the Morse code version of your text.

## Supported Characters

The program can convert the following types of characters:

All uppercase and lowercase letters (A to Z)
All digits (0 to 9)
Common punctuation marks (comma, period, question mark, forward slash, hyphen, parentheses)
Spaces (converted to forward slashes in Morse code)

## Example

If you enter: Hello World

The program will output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

## Technical Details

The program works by using a dictionary that maps each character to its Morse code representation. It converts your input to uppercase, then looks up each character in the dictionary and builds the Morse code string. Characters that are not in the dictionary are simply skipped.

## Files in This Project

main.py: The main Python program file that contains all the conversion logic
LICENSE.dat: The MIT license file for this project
README.md: This file, containing project documentation
requirements.txt: File describing the project requirements

## License

This project is licensed under the MIT License. See the LICENSE.dat file for full details.
