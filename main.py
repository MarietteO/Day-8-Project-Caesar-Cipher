from art import logo

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def get_valid_mode():
    valid_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if valid_mode not in ["encode", "decode"]:
        return False
    else:
        return valid_mode


def chosen_mode(user_mode, user_message, user_shift_number):
    letter_list = [letter for letter in user_message]
    new_message = ""
    while user_mode not in ["encode", "decode"]:
        user_mode = input("Invalid mode. Please enter 'encode' or 'decode': ")
    for letter in letter_list:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            if user_mode == "encode":
                user_shift_number = user_shift_number*1
            elif user_mode == "decode":
                if user_shift_number > 0:
                    user_shift_number = user_shift_number*-1
                else:
                    user_shift_number = user_shift_number*1
            else:
                return False
            new_index = old_index + user_shift_number
            encrypted_letter = alphabet[new_index]
            new_message += encrypted_letter
        else:
            encrypted_letter = letter
            new_message += encrypted_letter
    return new_message


print(logo)

loop = True
while loop:
    mode = get_valid_mode()
    if mode:
        message = input("Type your message: \n")
        shift_number = int(input("Type the shift number: \n"))
        encoded_message = chosen_mode(mode, message, shift_number)
        print(f"Your new message is {encoded_message}.")
    else:
        print("That is not a valid option. Please try again.")
