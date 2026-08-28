# Day 13: Network Communication & Log Parsing
**Date:** August 28, 2026

## 🎯 Today's Focus
Today I learned how computers talk to each other over networks, how to navigate Linux without getting lost, and how to use Python to chop up messy data.

## 🐧 OverTheWire: Level 14 -> Level 15
**The Challenge:** The password wasn't in a file. I had to prove my identity to a "security guard" running on a specific port.
**The Tool:** `nc` (Netcat) - The ultimate hacker networking tool.
**The Concept:** Client-Server Communication. I used a pipe (`|`) to take my current password and feed it directly into a listening port.
**Command Used:**
```bash
cat /etc/bandit_pass/bandit14 | nc localhost 30000
```

## 🧭 Linux Navigation Masterclass
I reviewed how to explore servers like a real hacker without getting trapped in folders:
* `cd ..` : Go back out one folder (parent directory).
* `cd ~` : Teleport back to the home folder.
* `pwd` : Print Working Directory (tells me exactly where I am).
* `ls /etc` : Look inside system folders to find configuration files.

## 🐍 Python: The Log Slicer
I learned how to extract specific data from messy server logs using string manipulation. This is exactly how Security Analysts build Intrusion Detection Systems to find attacker IPs.

**The Code:**
```python
# A messy server log
log = "Failed password for bandit14 from 192.168.1.50 port 22"

# Chop it into a list of words using .split()
words = log.split()

# Python starts counting at ZERO. 
# Index 3 is the username, Index 5 is the IP address.
username = words[3]
ip_address = words[5]

print("Target:", username)
print("Attacker IP:", ip_address)
```

## 💡 Big Picture Realization
I learned today that every major cybersecurity tool is just built using basic Python logic: Variables, Loops, `if/else` statements, and string manipulation. I am not just learning Python syntax; I am learning how to automate hacker workflows.
