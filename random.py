import random

def generate_random_number():
    return random.randint(1, 100)  # Change range if needed

if __name__ == "__main__":
    number = generate_random_number()
    print("Random number:", number)
