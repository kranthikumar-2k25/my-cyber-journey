# Day 19: Cron Jobs, Python .split(), & CCNA Episode 3
**Date:** September 04, 2026

## 🐧 OverTheWire: Level 21 -> 22 (Level 22 saved for tomorrow)

### Level 21: The Robot and the Locker (Cron Jobs)
**The Concept:** `cron` is Linux's automatic alarm clock. It runs scripts at scheduled intervals.

**The Hack:**
1. Found the schedule: `cat /etc/cron.d/cronjob_bandit22`
2. Read the script it executes: `cat /usr/bin/cronjob_bandit22.sh`
3. The script copies the Level 22 password into a hidden file in `/tmp/`
4. Stole the password: `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`

**The Plain English Story:**
- `cron` = The building's automatic alarm clock
- `/etc/cron.d/` = The sticky note on the alarm clock that says what to do
- `/usr/bin/cronjob_bandit22.sh` = The instruction manual the robot follows
- `/tmp/filename` = The locker where the robot drops off the secret password

**Key Takeaway:** I stopped blindly copying commands and actually read the script line by line. I understood the "why" behind every step.

---

## 🐍 Python: .split(), Indexing, and \n

### The Core Concept
Learned that Python's `.split()` method is the exact equivalent of Linux's `cut` command when chopping text.

**Linux way:** `echo "text" | cut -d ' ' -f 1`
**Python way:** `text.split()[0]`

### The Code
```python
raw_shredder_output = "8ca319486bfbbc3663ea0c813483639d  -"

# .split() chops the string into a list at every space
# [0] grabs the first item from that list
barcode = raw_shredder_output.split()[0]

print(barcode)
# Output: 8ca319486bfbbc3663ea0c813483639d
