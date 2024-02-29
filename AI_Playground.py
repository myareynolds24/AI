# Programmer: Mya Reynolds
# Date: 2.29.24
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology \n")



import random
import string

def generate_random_password(length):
    """Generates a random password."""
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use random.choices to select a random character for each position in the password
    password = ''.join(random.choices(characters, k=length))
    return password

# Specify the desired length of the password
password_length = 12  # You can change this to any length you prefer

# Generate and print the password
random_password = generate_random_password(password_length)
print(f"Your random password is: {random_password}")


import random

def generate_random_string(length):
    """Generates a random string using only 'p', 'o', 'k', 'i', 'e'."""
    # Define the possible characters in the string
    characters = 'mya'
    # Use random.choices to select a random character for each position in the string
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

# Specify the desired length of the string
string_length = 10  # You can change this to any length you prefer

# Generate and print the string
random_string = generate_random_string(string_length)
print(f"Your random string is: {random_string}")