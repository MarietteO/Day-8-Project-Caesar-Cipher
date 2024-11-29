#A simpler solution.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def compute(action, msg, shift_num):
    new_word = ""
    shift_num = int(shift_num)
    for letter in msg:
        if letter in alphabet:
            ind = alphabet.index(letter)
            new_ind = ind + shift_num if action == "e" else ind - shift_num
            new_letter = alphabet[new_ind]
            new_word += new_letter
        else:
            new_word += letter
    return new_word


print("Welcome to the Caesar Cipher.")

while True:
    choice = input("Do you want to encode or decode? Type e or d: ").lower()
    if choice != "e" and choice != "d":
        print("That answer is not valid.")
    else:
        message = input("Type your message: ")
        shift_number = input("Please type the shift number: ")
        if shift_number.isdigit():
            print(f"Your answer is {compute(choice, message, shift_number)}.")
            cont = input("Type q to quit, or anything else to encode/decode another word: ").lower()
            if cont == "q":
                break
        else:
            print("That answer is not valid.")
