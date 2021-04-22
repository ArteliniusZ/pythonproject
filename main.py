username = "developer1";
password = "hackme";

print("This program checks if username and password are correct\n");

input_username = input("Please enter username: ");
input_password = input("Please enter password: ");
is_username_valid = username == input_username
is_password_valid = password == input_password

if not (is_username_valid and is_password_valid):
    if not is_username_valid:
        print("Invalid username")
    if not is_password_valid:
        print("Invalid password")
    exit(1)

if is_username_valid and is_password_valid:
    print("Welcome " + input_username + ", you are authorized")
    shut_down = input("Do you want to shut down the computer?: ")
    if shut_down == 'yes':
        print("Have a nice day!")
    elif shut_down == 'no':
        admin = input("Do you want to become an admin? ")
        if admin == 'yes':
            print("Nice!")
        elif admin == 'no':
            print("OK")
        else:
            print("What?")
else:
    print("Have a nice day!")
