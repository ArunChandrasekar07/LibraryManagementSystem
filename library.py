def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    correct_username = "admin"
    correct_password = "admin123"

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome to Library Management System.")
    else:
        print("Invalid username or password. Please try again!")

login()
