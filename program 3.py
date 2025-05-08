import random
import string 

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure the password contains at least one lowercase, one uppercase, one digit, and one special character
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

try:
    length = int(input("Enter desired password length: "))
    generated_password = generate_password(length)
    
    if generated_password:
        print("\nYour Secure Password is:")
        print(generated_password)

except ValueError:
    print("Please enter a valid number.")
