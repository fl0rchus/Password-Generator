import random
import string

print("Password generator")

letters = string.ascii_letters
numbers = string.digits

def pass_leng():
    length = int(input("Length of the password: "))
    return length

def generator(length):
    password = f"{letters}{numbers}"
    password = list(password)
    random.shuffle(password)

    new_password = random.sample(password, length)
    new_password = "".join(new_password)

    return new_password

def main():
    print(generator(pass_leng()))
    question = input("Do you want to generate another password? (Yes / No) ")
    if question == "Yes" or question == "yes":
        print(generator(pass_leng()))
    elif question == "No" or "no":
        print("Finish")

main()
