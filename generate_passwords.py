import random
import string

def generate_password_list(num_passwords, password_length):
    """
    Generate a list of random passwords.

    Args:
        num_passwords (int): Number of passwords to generate.
        password_length (int): Length of each password.

    Returns:
        list: A list containing the generated passwords.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(password_length))
        passwords.append(password)
    return passwords

def main():
    """Example usage when running the script directly."""
    num_passwords_to_generate = 5
    desired_password_length = 12
    generated_password_list = generate_password_list(num_passwords_to_generate, desired_password_length)

    print(f"Generated {num_passwords_to_generate} passwords of length {desired_password_length}:")
    for p in generated_password_list:
        print(p)

# This ensures the script runs the example only when executed directly,
# but allows importing generate_password_list in other scripts.
if __name__ == "__main__":
    main()
