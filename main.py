from time import sleep

users = [
    ("admin", "admin"),
    ("turbo_hacker", "hackme"),
    ("qa_tester", "123test"),
    ("a_simple_mortal", "password"),
    ("dog", "bark-bark")
]


#username = "developer1";
#password = "hackme";
auth_entries = 3;

print("This program checks if username and password are correct\n");
while auth_entries > 0:
    input_username = input("Please enter username: ");
    input_password = input("Please enter password: ")

    is_username_valid, is_password_valid = False, False
    for username,  password in users:
        if input_username == username:
            is_username_valid = username == input_username
            is_password_valid = password == input_password
            break


    if is_username_valid and is_password_valid:
        break
    else:
        auth_entries -= 1
    if not (is_username_valid and is_password_valid):
        if not is_username_valid:
            print("Invalid username")
        if not is_password_valid:
            print("Invalid password")
        if auth_entries == 0:
            print("Tries have expired")
            exit(1)

print("Welcome " + input_username + ", you are authorized")
while True:
    print("Please select something: ")
    print("[+] Create new user (1)")
    print("[+] List users (2)")
    print("[+] Hack pentagon (3)")
    print("[+] Exit (4)")

    choice = input(">> ")
    if choice == "1":
        input_username = input("Enter new user's username")
        input_password = input("Enter new user's password")
        user_already_exists = False
        for username, password in users:
            if username == input_username:
                user_already_exists = True
                break
        if user_already_exists:
            print(f"Conflict: User with username {input_username} already exists")
            continue
        users.append((input_username, input_password))
        print(f"[+] User {input_username} has been added succesfully")
        continue
    elif choice == "2":
        order_number = 1
        for username, password in users:
            print(f"{order_number}) {username} - {'*' * len(password)}")
            order_number += 1
    elif choice == "3":
        print("Hacking pentagon....")
        sleep(5)
    elif choice == "4":
        print("Exit the program")
        exit(0)

    else:
        print("No avalaible option")
