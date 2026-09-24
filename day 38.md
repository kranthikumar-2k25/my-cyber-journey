# Day 38: The Night Shift Protocol

## 🐧 BANDIT (2 Levels)

### Level 18: The Boot-Out
- **Challenge:** Server kicks you out instantly on SSH login.
- **Hack:** Append command to SSH string to execute during login handshake.
- **Command:** `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"`
- **Concept:** SSH Command Execution

### Level 19: The SUID Ghost
- **Challenge:** Need to read Level 20 password without being Level 20.
- **Hack:** Use SUID binary owned by next level user.
- **Command:** `./bandit20-do cat /etc/bandit_pass/bandit20`
- **Concept:** SUID Privilege Escalation

---

## 🕸️ NATAS SPEEDRUN (Levels 0-10)

| Level | Challenge | Hack |
|-------|-----------|------|
| 0 | Open Door | CTRL+U (View Source) |
| 1 | Fake Lock | CTRL+U / view-source: URL |
| 2 | Image Trick | Directory listing `/files/users.txt` |
| 3 | Hacker Map | `robots.txt` reveals hidden folder |
| 4 | The Bouncer | `curl -e` forges Referer header |
| 5 | Invisible Wristband | `curl -b "loggedin=1"` forges cookie |
| 6 | Leaky Blueprint | Browse directly to `/includes/secret.inc` |
| 7 | The Jailbreak | Path Traversal `../../../../etc/natas_webpass/natas8` |
| 8 | Encoding Maze | Bash pipeline: `xxd -r -p | rev | base64 -d` |
| 9 | Puppet Master | Command Injection: `; cat /etc/natas_webpass/natas10 #` |
| 10 | Regex Blockade | `"" /etc/natas_webpass/natas11` tricks grep |

---

## 🔥 CYBER THEORY: XSS vs COMMAND INJECTION

| Attack | Target | Location |
|--------|--------|----------|
| Command Injection | Server's Linux Terminal | Backend |
| XSS (Cross-Site Scripting) | User's Web Browser | Frontend |

### XSS Concept
- Website blindly pastes user input onto screen.
- Hacker injects `<script>alert('HACKED')</script>`.
- Victim's browser executes the JavaScript.
- Used to steal cookies/sessions.

---

## 🌐 CCNA: ARP SPOOFING (Man-in-the-Middle)

### ARP (Address Resolution Protocol)
- Protocol that matches **IP Address** to **MAC Address**.
- Router shouts: "WHO HAS IP 192.168.1.15?"
- Victim replies: "I do! My MAC is 00:1A:2B..."

### ARP Spoofing Attack
- Hacker lies to **Router**: "My MAC belongs to the Victim's IP."
- Hacker lies to **Victim**: "My MAC belongs to the Router's IP."
- Both believe the hacker. All traffic flows through hacker.
- Hacker reads data, then forwards it (Man-in-the-Middle).
- **Why coffee shop Wi-Fi is dangerous.**

---

## 🐍 PYTHON: FOR LOOPS

### The Conveyor Belt Analogy
```python
ports = [80, 443, 22]

for port in ports:
    print("scanning_target_ports: " + str(port))
