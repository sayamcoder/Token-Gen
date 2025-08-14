# token_generator.py

import secrets
import string

def generate_token(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generates a cryptographically secure, random token with configurable character sets.

    This function uses the 'secrets' module, making it suitable for generating
    API keys, session tokens, password reset links, and other security-sensitive material.

    Args:
        length (int): The desired length of the token. Defaults to 16.
        use_uppercase (bool): Whether to include uppercase letters (A-Z).
        use_lowercase (bool): Whether to include lowercase letters (a-z).
        use_digits (bool): Whether to include digits (0-9).
        use_symbols (bool): Whether to include punctuation symbols (!"#$%&'...).

    Returns:
        str: The securely generated random token.
        
    Raises:
        ValueError: If all character sets are disabled, as no token can be formed.
    """
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("Cannot generate token. At least one character set must be enabled.")

    # Generate the token using a secure method
    token = "".join(secrets.choice(character_pool) for _ in range(length))
    
    return token