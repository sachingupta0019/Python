def isStrongPassword(password):

    if len(password) < 6:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '@#!&%*()_+' for char in password):
        return False
    return True

print("Weak Password", isStrongPassword('sachin001'))
print(isStrongPassword('S@ch!n001'))



origin_pass = 'aschin001@'
i=3
while i != 0:
    password = input("Enter password : ")
    if password == origin_pass:
        print("Login Successfull")
        break
    else:
        print(f"you have {i} attempts left")
        i -= 1
print("You have exceeded the limit")