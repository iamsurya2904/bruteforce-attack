import itertools
import string

def brute_force(target_password):
    characters = string.ascii_lowercase + string.digits
    for length in range(1, 6):  # Limiting to 5 characters for demonstration purposes
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            print(f"Trying password: {guess}")
            if guess == target_password:
                print(f"Password found: {guess}")
                return guess
    return None

if __name__ == "__main__":
    target_password = "ab123"  # Replace with your target password for testing
    found_password = brute_force(target_password)
    if found_password:
        print(f"Success: The password is {found_password}")
    else:
        print("Failed: Password not found")
