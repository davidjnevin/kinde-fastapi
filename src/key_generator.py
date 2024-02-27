import string
import secrets


def generate_random_string(length=43):
    """Generates a cryptographically secure random string of the specified length.

    Args:
      length: The desired length of the random string (default: 43).

    Returns:
      A cryptographically secure random string of the specified length.
    """

    # Define the character set to use for generating the random string.
    # This includes uppercase and lowercase letters, digits, and special characters.
    char_set = string.ascii_letters + string.digits + string.punctuation

    # Use the secrets module's token_bytes() function to generate cryptographically
    # secure random bytes. Convert the bytes to a string using the appropriate encoding.
    random_bytes = secrets.token_bytes(
        length // 2 + 1
    )  # Generate enough bytes for the desired string length
    random_string = random_bytes.hex()[
        : length
    ]  # Convert to hex string and slice to get the desired length

    return random_string


# Generate a random string of length 43
random_string = generate_random_string()

# Print the generated random string
print(random_string)
