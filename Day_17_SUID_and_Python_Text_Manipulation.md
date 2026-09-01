# Day 17: Auto-Logout Bypass, SUID Binaries, & Python Text Manipulation
**Date:** September 02, 2026

## 🧠 The 35-Question Master Gauntlet
Completed the memory gauntlet. Locked in Linux commands, Python logic, and CCNA networking (OSI layers, Switch vs Router, MAC vs IP).

## 🐧 OverTheWire: Level 18 & 19

### Level 18: The Auto-Logout Trap
**Challenge:** The server kicks you out instantly upon logging in due to a modified `.bashrc` file.
**Hacker Bypass:** Execute a remote command over SSH without opening an interactive shell.
**Command:** `ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme`

### Level 19: SUID Binaries (Privilege Escalation)
**Challenge:** Use a setuid binary to read the next level's password.
**Concept:** A file with the SUID bit (`s` in permissions, e.g., `-rwsr-x---`) runs with the permissions of the file's *owner*, not the user executing it. We used it to read a file as `bandit20`.
**Command:** `./bandit20-do cat /etc/bandit_pass/bandit20`

## 🐍 Python Class: Simulating Linux Tools
Learned how to simulate Linux's `awk` and `tr` commands using Python string manipulation.
*   **Linux `tr -d '\r'`** (The Eraser) = **Python `.replace("\r", "")`** (Removes invisible Windows ghost characters).
*   **Linux `awk '/BEGIN/,/END/'`** (The Scissors) = **Python `.split("\n")` + `if/else` switch** (Cuts out only the text between markers).
