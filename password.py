import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 characters!")
        return
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation 
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    return ''.join(password)
print("Generated Password:", generate_password(12))
