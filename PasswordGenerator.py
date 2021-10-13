import string
import random
letters = list(string.ascii_letters) 
digits=list( string.digits) 
special_characters=list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():

    length = int(input("Enter password length: "))
    letters_count=int(input("How many letters in the password? "))
    digits_count=int(input("How many digits in the password? "))
    special_characters_count=int(input("How many special characters in the password? "))

    characters_count=letters_count+digits_count+special_characters_count

    if characters_count > length:
	    print ("Characters total count is greater than the password length")
	    return

    password=[]
    for i in range(letters_count):
        password.append(random.choice(letters))
    for i in range(digits_count):
        password.append(random.choice(digits))
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        for i in range( length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_random_password()

