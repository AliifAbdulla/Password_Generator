"""
A simple command-line password generator.

This script prompts the user for desired password length and character types
(letters, numbers, symbols) and then generates a secure, random password.
"""
import random
import string

def generate_password(length=12, include_letters=True, include_numbers=True, include_symbols=True):
    """
    Generates a random password based on user-defined criteria.

    Args:
        length (int): The desired length of the password.
        include_letters (bool): Whether to include lowercase and uppercase letters.
        include_numbers (bool): Whether to include digits.
        include_symbols (bool): Whether to include special symbols.

    Returns:
        str: The generated password.
    """
    # Create the pool of characters based on user's choices
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Check if at least one character type was selected
    if not characters:
        return "Error: Please select at least one character type for your password."

    # Generate the password by randomly selecting from the character pool
    password = ''.join(random.choices(characters, k=length))
    return password

def get_user_input():
    """
    Collects user input for password generation settings.
    """
    print("Welcome to the Python Password Generator!")
    print("---------------------------------------")

    while True:
        try:
            # Get the desired password length
            length_input = int(input("Enter desired password length (e.g., 12): "))
            if length_input <= 0:
                print("Length must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask the user which character types to include
    include_letters = input("Include letters? (yes/no): ").lower().startswith('y')
    include_numbers = input("Include numbers? (yes/no): ").lower().startswith('y')
    include_symbols = input("Include symbols? (yes/no): ").lower().startswith('y')

    # Generate and display the password
    password = generate_password(length_input, include_letters, include_numbers, include_symbols)
    print("\nGenerated Password: ", password)

# Run the main function when the script is executed
if __name__ == "__main__":
    get_user_input()
