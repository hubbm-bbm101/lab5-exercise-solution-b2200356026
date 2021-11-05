userEmail = input("Enter your email:")

def email_controller():
    valid_email = False
    if "@" in userEmail and "." in userEmail:
        valid_email = True
    else:
        valid_email = False

    if valid_email == False:
        print("Your email is invalid")
    else:
        print("Your email is valid")

email_controller()



