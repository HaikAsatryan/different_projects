from random import randint

# The goal of this project is to create password generator, generating 15x random 20 character password!

characters = range(33, 127)

generated_password = []


def password_generator():
    for i in range(20):
        random_index = randint(0, len(characters) - 1)
        unicode_integer = characters[random_index]
        unicode_character = chr(unicode_integer)
        generated_password.append(unicode_character)
    print(''.join(generated_password))


for i in range(15):
    password_generator()
    generated_password = []