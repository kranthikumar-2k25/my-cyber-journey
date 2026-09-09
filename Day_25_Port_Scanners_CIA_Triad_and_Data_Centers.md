# Day 25: Port Scanners, CIA Triad & Data Centers
**Date:** September 10, 2026

## 🐧 OverTheWire: Level 26 -> 27

### The Challenge: The SUID Binary
**The Concept:** Once inside Level 26, there is a file called `bandit27-do`. Normal users can't read other users' password files.
**The Hack:** The file has the **SUID bit** set. This Linux permission means the file runs with the permissions of its OWNER, no matter who types it.
**Key Commands:**
- `ls -la` (check for files with special permissions)
- `./bandit27-do cat /etc/bandit_pass/bandit27` (use the tool to read the secret file)

### The Big Lesson: The Golden Formula
`[Hidden Tool] + [Command] + [Secret File] = Privilege Escalation`
Hackers don't always break passwords; they look for broken tools left behind by admins to bypass the rules.

---

## 🌐 CCNA: Episode 6 (Data Center Designs)

### Old vs. New Network Design
As data centers grew, the old 3-Tier design choked on "East-West" traffic (servers talking to servers).

| Design | Layers | Hop Count | Problem |
|---|---|---|---|
| **OLD (3-Tier)** | Access, Distribution, Core | Many hops | Bottlenecks when servers talk to each other. |
| **NEW (Spine-Leaf)** | Leaf, Spine | Exactly 2 hops | Predictable, ultra-fast East-West traffic. |

---

## 🔥 Cybersecurity: The CIA Triad

Every security control in the world protects one of three pillars:

| Pillar | Definition | Broken When... |
|---|---|---|
| **Confidentiality** | Only authorized people see it | A hacker steals the database. |
| **Integrity** | Data hasn't been secretly changed | A hacker alters your bank balance. |
| **Availability** | System is up and running | A DDoS attack crashes the site. |

---

## 🐍 Python: `if` vs `elif` & Port Scanners

### The Concept
- **Indentation:** Tells Python what is INSIDE the loop. If it's outside, it only runs once at the end.
- **`elif`:** Prevents double-triggering. If you use multiple `if` statements, Python checks ALL of them. `elif` means "only check this if the previous one was False".

### The Code
```python
target_ports = [21, 22, 80, 443, 3306, 8080]

for port in target_ports:
    print(f"Scanning port {port}...")
    
    if port == 3306:
        print("⚠️ MySQL is open!")
    elif port == 8080:
        print("🔥 Tomcat is open!")
    else:
        print("✅ Port is closed.")
