print("SECURE EMPLOYEE ACCOUNT SYSTEM")

accounts = {}
number_of_accounts = int(input("Enter number of accounts to create: "))

for i in range(number_of_accounts):
    print("Account", i + 1)
    username = input("Enter username: ")

    while True:
        password = input("Enter password: ")
        uppercase = False
        lowercase = False
        digit = False
        special = False
        space = False
        for ch in password:
            if ch >= 'A' and ch <= 'Z':
                uppercase = True
            elif ch >= 'a' and ch <= 'z':
                lowercase = True
            elif ch >= '0' and ch <= '9':
                digit = True
            elif ch == ' ':
                space = True
            else:
                special = True
        valid = True
        if len(password) < 8:
            valid = False
        if uppercase == False:
            valid = False
        if lowercase == False:
            valid = False
        if digit == False:
            valid = False
        if special == False:
            valid = False
        if space == True:
            valid = False
        if valid == True:
            break

        print("Password rejected")
        if len(password) < 8:
            print("Password must contain at least 8 characters")
        if uppercase == False:
            print("Password must contain at least one uppercase alphabet")
        if lowercase == False:
            print("Password must contain at least one lowercase alphabet")
        if digit == False:
            print("Password must contain at least one digit")
        if special == False:
            print("Password must contain at least one special character")
        if space == True:
            print("Password must not contain any space")
        print("Please enter the password again")

    confirm_password = input("Confirm password: ")
    while confirm_password != password:
        print("Passwords do not match")
        confirm_password = input("Please enter the confirm password again: ")
    accounts[username] = password
    print("Account created successfully")

print("EMPLOYEE LOGIN")
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in accounts:
        if accounts[username] == password:
            print("Login successful")
            print("Welcome", username)
            break
        else:
            print("Invalid username or password")
    else:
        print("Invalid username or password")
    attempts = attempts + 1
    if attempts < max_attempts:
        print("Attempts remaining:", max_attempts - attempts)
    else:
        print("Access Denied")
        print("Maximum login attempts exceeded")