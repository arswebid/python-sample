def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Example usage
username = input("Username: ")
password = input("Password: ")
if login(username, password):
    print("Login successful!")
else:
    print("Login failed.")
