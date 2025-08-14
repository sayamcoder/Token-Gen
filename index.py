# main.py

# Import the specific function we need from our other file
from token_generator import generate_token

def demonstrate_usage():
    """
    Shows various examples of how to use the token generator.
    """
    print("--- Token Generator Demonstration ---")

    # 1. Generate a standard 16-character token (letters and numbers)
    default_token = generate_token()
    print(f"Default 16-char token: {default_token}")

    # 2. Generate a long, 32-character token for higher security
    long_token = generate_token(length=32)
    print(f"Long 32-char token:    {long_token}")

    # 3. Generate a numeric-only PIN code
    pin_code = generate_token(length=6, use_uppercase=False, use_lowercase=False, use_digits=True)
    print(f"6-digit PIN code:      {pin_code}")

    # 4. Generate a complex password with symbols
    complex_password = generate_token(length=20, use_symbols=True)
    print(f"Complex 20-char pass:  {complex_password}")

    # 5. Generate a lowercase-only token (e.g., for a unique URL slug)
    slug_token = generate_token(length=8, use_uppercase=False, use_digits=False)
    print(f"URL-friendly slug:     {slug_token}")

    # 6. Demonstrate the error handling
    try:
        print("\nAttempting to generate a token with no character sets...")
        invalid_token = generate_token(use_uppercase=False, use_lowercase=False, use_digits=False)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")


# This block ensures the code runs only when the script is executed directly
if __name__ == "__main__":
    demonstrate_usage()