Day 2 Python practice:
- Implemented user credential verification using conditional `if/else` logic
- Handled dynamic user inputs via `input()` for target IP and alias assignment
- Formatted console output for basic access logging and alert states

print("--- TARGET ACQUISITION SYSTEM ---")

password = input("enter the password: ")

if password == "l023r123":
    print("access granted. welcome to mainframe")
    user_id = input("what is your alias: ")
    target_ip = input("what is the ip address: ")
    print(user_id, "is attacking", target_ip)
else:
    print("access denied. alerting user.")
