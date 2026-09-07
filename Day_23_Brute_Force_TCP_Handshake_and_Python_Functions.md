# Day 23: Brute Force Attacks, TCP Handshake & Python Functions
**Date:** September 08, 2026

## 🐧 OverTheWire: Level 24 -> 25

### The Challenge: The PIN Code Checker
**The Concept:** A daemon listens on port 30002. It wants the Level 24 password AND a secret 4-digit PIN. There is no clue. The only way in is to try all 10,000 combinations.

**The Hack:** I built a Bash loop that generates every PIN from 0000 to 9999, combines it with the password, and pipes all 10,000 attempts into the daemon through a single netcat connection.

**Key Commands:**
- `nc localhost 30002` (connect to the daemon)
- `for i in {0000..9999}; do echo "PASSWORD $i"; done | nc localhost 30002` (brute force all PINs)

### The Big Lesson: Automation & TCP Efficiency
A human would spend hours typing 10,000 PINs. A loop does it in seconds. And by piping everything into ONE netcat connection, we only do ONE TCP handshake. Opening netcat 10,000 times would mean 10,000 handshakes. One stream, one handshake, maximum speed.

---

## 🛠️ Custom Lab: Mystery PIN (5-Digit Brute Force)

### The Mission
Built my own brute-force server from scratch. Upgraded to 5 digits (100,000 combinations) and changed the password.

### The Bug I Found
My script failed because I generated a 5-digit number but padded it with 4 digits (`%04d`). The PIN was stored wrong.

### The Fix
Changed `printf "%04d"` to `printf "%05d"`. One character. That was the entire bug.

### The Big Lesson: Debugging IS Hacking
Every error is a clue. I didn't quit. I read the code, found the mismatch, and fixed it. Attention to detail is the difference between a broken script and a working exploit.

---

## 🔥 Cybersecurity Masterclass: Hashing vs Encryption vs Encoding

| Concept | Analogy | Reversible? |
|---|---|---|
| **Encoding** (Base64) | Translation | Yes, no key needed |
| **Encryption** (AES-256) | Locked Box | Yes, BUT needs the key |
| **Hashing** (SHA-256) | Shredder | NO, never |

**Dictionary Attack:** Hash every word in a wordlist (like RockYou.txt), compare to stolen hashes. When they match, you found the password.

**Salting:** Companies add random characters to passwords BEFORE hashing. This defeats dictionary attacks because pre-computed hashes won't match.

**Avalanche Effect:** Changing ONE character completely changes the entire hash. You can never guess how "close" two passwords are.

---

## 🌐 CCNA: Episode 5 (TCP Handshake & Ports)

### The TCP 3-Way Handshake
| Step | Flag | Meaning |
|---|---|---|
| 1 | SYN | "Hey, can we talk?" |
| 2 | SYN-ACK | "Yes! Can YOU hear ME?" |
| 3 | ACK | "Yes! Let's go!" |

TCP waits for confirmation. UDP skips the handshake entirely.

**Critical Ports:**
- HTTP = Port 80 (unencrypted)
- HTTPS = Port 443 (encrypted)

---

## 🐍 Python: Functions (`def`)

### The Concept
A function is a reusable tool. Define it once, call it as many times as you want. This is the DRY Principle (Don't Repeat Yourself).

```python
def check_login(username, password):
    if username == "neo" and password == "redpill":
        print("\nAccess Granted")
    else:
        print("\nAccess Denied")

check_login("neo", "redpill")
check_login("neo", "wrongpassword")
