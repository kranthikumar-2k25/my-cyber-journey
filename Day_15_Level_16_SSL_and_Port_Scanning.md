# Day 15: Conquering OverTheWire Level 16
**Date:** August 30, 2026

## 🐧 OverTheWire: Level 15 -> Level 16 -> Level 17
**The Challenge:** Find a hidden SSL port between 31000 and 32000, extract a private SSH key, and use it to log into Level 17.

### 🧰 The Hacker Toolkit Learned Today:
1. **`nmap` (Network Mapper):** The ultimate port scanner.
   * `nmap -sV -p 31000-32000 localhost` (Scans a specific range of doors and checks what services are running inside).
   * *Trap found:* Port 31518 was an "echo" server (decoy). Port 31790 was the real SSL server.

2. **`openssl`:** The cryptography tool.
   * `openssl s_client -connect localhost:31790 -quiet` (Knocks on the SSL encrypted door and hides the messy certificate text).

3. **Text Manipulation (The Scissors and Eraser):**
   * The server output was messy. It included the word "Correct!" and invisible Windows ghost characters (`\r`).
   * **`awk '/-----BEGIN/,/-----END/'`**: The Scissors. Cuts out ONLY the text between the BEGIN and END markers.
   * **`tr -d '\r'`**: The Eraser. Deletes the invisible Windows line-break characters so the math key isn't corrupted.

4. **`chmod 600`:** Locking down Linux file permissions.
   * SSH will refuse to use a private key if other users on the server can read it. `chmod 600` makes it private.

## 🧠 The Big Lesson
You cannot always trust raw terminal output. Data often contains hidden garbage (like the word "Correct!" or invisible `\r` characters). A true hacker knows how to clean and sanitize data before feeding it into another tool.

## 🐍 Python Class
*Paused for tomorrow.* Next up: More Python string manipulation and the 35-Question Master Gauntlet!
