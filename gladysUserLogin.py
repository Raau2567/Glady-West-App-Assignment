def login():
    """
    Prompts the user for a login (email address) and password, and returns the login if it's a valid email address.

    Returns:
        str: The user's login (email address).
    """
    login_successful = False
    while not login_successful:
        # Ask the user for login (email address)
        login_email = input("Enter your email address: ")

        # Check if the entered login is a valid email address
        if not validate_email(login_email):
            print("Invalid email address. Please enter a valid email address.")
            continue

        # Ask the user for a password
        password = input("Enter your password: ")
        # For simplicity, any password is considered valid

        # Set login_successful to True to break out of the loop
        login_successful = True

    return login_email


def validate_email(email):
    """
    Validates if the given string is a valid email address.

    Args:
        email (str): The string to validate.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    # Check if the string contains '@' symbol
    if '@' not in email:
        return False

    # Split the string by '@' and check if it has exactly two parts
    parts = email.split('@')
    if len(parts) != 2:
        return False

    # Check if the domain part contains at least one dot ('.')
    if '.' not in parts[1]:
        return False

    # If all conditions are satisfied, return True
    return True


# Example usage
if __name__ == "__main__":
    user_login = login()
    print("Login successful. Welcome,", user_login)
