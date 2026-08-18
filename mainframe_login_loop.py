print("--- SECURE MAINFRAME SYSTEM ---")

while True:
    password = input("what is your password: ")

    if password == "loser123":
        print("access granted.")
        user_id = input("what is your id: ")
        target_ip = input("what is ip address: ")
        print(user_id, "is attacking", target_ip)
        break
    else:
        print("access denied. try again noob\n")
