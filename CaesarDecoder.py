alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_alphabet = [letter.lower() for letter in alphabet]

og = input("Enter the phrase you want to decode:")

shift = int(input("Enter the shift if you know it, or if you don't, enter '1' if you don't:"))
shiftcheck = shift + 27

raw = list(og)
result = ""

yn = ""
while True:
    if shift >= shiftcheck:
        print("Decoding failed")
        break
    result = ""
    for char in raw:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        elif char in lowercase_alphabet:
            position = lowercase_alphabet.index(char)
            new_position = (position + shift) % 26
            result += lowercase_alphabet[new_position]
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    print("Shift was: " + str(shift))
    print(result)
    yn= input("Is this correct? (y/n)")
    if yn == "y":
        print("Decoding succeeded")
        break
    shift = shift + 1

print("Exiting...")
