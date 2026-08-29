# Day 14: SSL Encryption & Advanced Python Slicing
**Date:** August 28, 2026 (Late Night Session)

## 🐧 OverTheWire: Level 15 -> Level 16
**The Challenge:** Send the password to a port, but the server demands it be encrypted using SSL.
**The Concept:** Plain text (`nc`) vs Encrypted text (`openssl`).
**The Command:** 
`cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -quiet`
*Pro-tip: The `-quiet` flag hides the messy certificate text and only shows the actual reply.*

## 🐍 Python: Splitting by Specific Characters
Yesterday I learned `.split()` chops text at spaces. Today I learned how to chop text at specific characters like colons (`:`) or commas (`,`). This is how real-world tools parse database leaks and CSV files.

**The Code:**
```python
record = "bandit16:hunter2:admin:192.168.1.99"
parts = record.split(":")

username = parts[0]
role = parts[2]

print(f"User {username} is an {role}.")
