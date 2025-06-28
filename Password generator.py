import random
import string

def password_type():    #writing a function to give about the details of password from user
    print("At first answer these questions:\n"  #ask the user about which type of password he wants
          "Enter 1 for 'Yes' and 0 for 'No'")
    upper = int(input("does your password contain uppercase letter?: "))
    #asking about if he wants uppercase letter or not
    special = int(input("does your password contain special character?: "))
    #asking if he wants special characters or not

    #we use ASCII code to make a list for each possible part
    if upper == 1:
        if special == 1:
            return list("qwertyuiopasdfghjklzxcvbnm[];./?{}!()@#$%^&*~_+QWERTYUIOPASDFGHJKLZXCVBNM<>1234567890")
        elif special == 0:
            return list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890")
        else:
            return "invalid input"
    elif upper == 0:
        if special == 1:
            return list("qwertyuiopasdfghjklzxcvbnm<>[]{}!@#$%^&*()1234567890")
        elif special == 0:
            return list("qwertyuiopasdfghjklzxcvbnm1234567890")
        else:
            return "invalid input"
    else:
        return "invalid input"

#defining a function to give the string length from the user
def password_length():
    try:
        length = int(input("Enter the length of your password: "))
        return length
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"

#defining a function to produce a random password
def generate_password(password_generator: list, length: int) -> str:
    password = ""
    for i in range(length):
        password += random.choice(password_generator)
    return password

#defining a function to check the password strength
def password_strength(password: str):
    count = 0   #to count how many important items we have in the password
    for letter in password:
        if letter.isupper():
            count += 1
            break

    for letter in password:
        if letter in string.punctuation:
            count += 1
            break

    if len(password) >= 12:
        count += 1

    if count == 0:
        print("Password is too weak")
    elif count == 1:
        print("Password is weak")
    elif count == 2:
        print("Password is strong")
    elif count == 3:
        print("Password is too strong")


#going through the main function
def main():
    print("Her there!\n"
          "Welcome to Password Generator")
    password_generator = password_type()
    while password_generator == "invalid input":
        print("You are only able to input 0 and 1 in the above questions!\n"
              "but here you may Entered an invalid input\n"
              "so please try again.")
        password_generator = password_type()

    length = password_length()
    while length == "ValueError":
        print("You have entered an invalied type of variable\n"
              "please type in an integer.")
        length = password_length()
    while length == "TypeError":
        print("You entered an invalied type of variable\n"
              "please type in an integer.")

    password = generate_password(password_generator, length)
    print(f"here your password is: {password}")
    print("And the strength of your password is:")
    password_strength(password)

main()