import argparse
from math import gcd

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alphabet = alphabet.lower()
digits = "0123456789"
shift_period = len(alphabet) * len(digits) // gcd(len(alphabet), len(digits))

def transform(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        elif char in lowercase_alphabet:
            result += lowercase_alphabet[
                (lowercase_alphabet.index(char) + shift) % len(lowercase_alphabet)
            ]
        elif char in digits:
            result += digits[(digits.index(char) + shift) % len(digits)]
        else:
            result += char
    return result

parser = argparse.ArgumentParser(description="Encode or decode a Caesar cipher.")
parser.add_argument(
    "--encode",
    action="store_true",
    help="encode the entered text instead of decoding it",
)
args = parser.parse_args()

if args.encode:
    text = input("Enter the phrase you want to encode:")
    shift = int(input("Enter the shift:"))
    print(transform(text, shift))
else:
    text = input("Enter the phrase you want to decode:")
    shift = int(
        input("Enter the shift if known, or enter '1' to try all shifts:")
    )

    for _ in range(shift_period):
        result = transform(text, -shift)
        print("Shift was: " + str(shift))
        print(result)
        if input("Is this correct? (y/n)") == "y":
            print("Decoding succeeded")
            break
        shift += 1
    else:
        print("Decoding failed")

print("Exiting...")
