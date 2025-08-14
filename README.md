# Python Secure Token Generator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A simple, powerful, and secure token generator module written in Python. It uses the built-in `secrets` module to generate cryptographically strong random tokens, making it suitable for security-sensitive applications like API keys, session identifiers, password reset links, and more.

## Key Features

-   🔐 **Cryptographically Secure**: Uses `secrets` module, not the predictable `random` module.
-   ⚙️ **Highly Configurable**: Easily control the token length and the character sets used (uppercase, lowercase, digits, symbols).
-   📦 **No External Dependencies**: Works out-of-the-box with the Python standard library.
-    modular **Clean & Reusable**: The core logic is separated into `token_generator.py` for easy integration into your own projects.
-   -   **Robust Error Handling**: Prevents generation of a token if no character sets are enabled.

## Project Structure

The project is intentionally split into two files to demonstrate a clean, modular approach:

```
token_project/
├── token_generator.py    # The core module with the token generation logic.
├── main.py               # An example script demonstrating how to use the module.
└── README.md             # This file.
```

## Installation

No external packages are required. Just clone the repository or download the files.

```bash
git clone https://github.com/sayam/Token-Gen.git
cd Token-Gen
```

## How to Use

Import the `generate_token` function from the `token_generator.py` module into your own project.

### Quick Start

Here are a few examples demonstrating how to use the function:

```python
from token_generator import generate_token

# 1. Generate a standard 16-character token (default settings)
api_key = generate_token()
print(f"API Key: {api_key}")
# Example Output: API Key: FwR8vK3aL7pZ9jN1

# 2. Generate a long, 32-character token for higher security
session_id = generate_token(length=32)
print(f"Session ID: {session_id}")
# Example Output: Session ID: mYc2xT6vQj9zEw4bHn8rGk5fD3aU7pWz

# 3. Generate a complex 20-character password including symbols
complex_password = generate_token(length=20, use_symbols=True)
print(f"Complex Password: {complex_password}")
# Example Output: Complex Password: J&e@8S)q$L#wP!zV(k<g

# 4. Generate a 6-digit numeric PIN code
pin_code = generate_token(length=6, use_uppercase=False, use_lowercase=False)
print(f"PIN Code: {pin_code}")
# Example Output: PIN Code: 815309

# 5. Generate a lowercase-only token for a unique URL slug
url_slug = generate_token(length=8, use_uppercase=False, use_digits=False)
print(f"URL Slug: {url_slug}")
# Example Output: URL Slug: kwefpoju
```

### Running the Demo

To see all the examples in action, you can run the `main.py` script directly from your terminal:

```bash
python main.py
```

## API Reference

### `generate_token()`

```python
generate_token(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = False
) -> str
```

**Parameters:**

| Parameter       | Type    | Default | Description                                              |
| --------------- | ------- | ------- | -------------------------------------------------------- |
| `length`        | `int`   | `16`    | The desired length of the generated token.               |
| `use_uppercase` | `bool`  | `True`  | Include uppercase letters (`A-Z`) in the character pool. |
| `use_lowercase` | `bool`  | `True`  | Include lowercase letters (`a-z`) in the character pool. |
| `use_digits`    | `bool`  | `True`  | Include digits (`0-9`) in the character pool.            |
| `use_symbols`   | `bool`  | `False` | Include punctuation symbols (`!@#$%^&*...`).             |

**Returns:**

-   `str`: A securely generated random token string.

**Raises:**

-   `ValueError`: If all character set flags (`use_uppercase`, `use_lowercase`, `use_digits`, `use_symbols`) are set to `False`.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/python-secure-token-generator/issues).

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
