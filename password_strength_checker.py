# A basic python project to evaluate the strength of password

import re
import getpass

def check_password_strength(password):
    strength = 0
    feedback = ""

    '''
    Check password based on four conditions:
    1. It must be atleast 8 characters long (+1)
    2. It must contain uppercase and lowercase letters (+1)
    3. It must contain numbers (+1)
    4. It must contain special characters (!@#$%^&*(),.?":{}|<>-_)
    '''

    if len(password) >= 8:
        strength += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1

    if re.search(r"\d", password):
        strength += 1

    if re.search("[!@#$%^&*(),.?\":{}|<>-_]", password):
        strength += 1

    # Provide feedback on the strength of the password evaluated based on the above four conditions
    if strength == 1:
        feedback = "Weak"
    elif strength == 2:
        feedback = "Moderate"
    elif strength == 3:
        feedback = "Strong"
    elif strength == 4:
        feedback = "Very Strong!"
    else:
        feedback = "Very Weak!"

    return strength, feedback

if __name__ == "__main__":
    password = getpass.getpass("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {feedback} ({strength}/4)")
