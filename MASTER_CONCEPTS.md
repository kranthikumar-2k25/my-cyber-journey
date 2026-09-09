# MASTER CONCEPTS LOG (Day 1 to Present)
*This is my long-term memory bank. The daily quiz pulls from this list.*
*NOTE: Days 1-17 are reconstructed. Adjust day numbers to match my real journey.*
*NOTE: Day 22 was skipped (busy day). No concepts added.*

---

## 🐧 LINUX (OverTheWire Bandit)

### Navigation & Reading
- Day 1: `ssh` (connect to server), `cat` (read file), `pwd` (where am I)
- Day 2: `ls` (list files), `cd` (change directory), spaces in filenames (`cat "my file.txt"`)
- Day 3: Hidden files (`ls -a`), `cd ..` (go up)

### Searching & Filtering
- Day 4: `find` (locate files), `find -type f`, `find -size`
- Day 5: `grep` (search text), `grep -v` (invert match - show everything EXCEPT the search term), `sort`, `uniq`
- Day 6: `strings` (read text from binary), `base64` (decode)
- Day 7: `tr` (translate/decode rot13), `xxd` / `hexdump` (read hex)

### Archives & Compression
- Day 8: `tar`, `gzip`, `bzip2` (extract archives)

### Networking & Permissions
- Day 9: `ssh` keys (passwordless login)
- Day 10: `nc` / netcat (talk to ports), connecting to ports
- Day 11: `nmap` (scan ports), SSL connections
- Day 12: `diff` (compare files)
- Day 13: SUID, `chmod` (permissions), `bandit20-do`
- Day 24: `scp` (Secure Copy) to exfiltrate files securely without corrupting Linux `\n` line endings
- Day 24: `icacls` (Windows command to lock down SSH key permissions, equivalent to `chmod 600`)

### Job Control & Automation
- Day 18: `&` (background), `CTRL-Z` (pause), `bg` (resume in background), `tmux` (split screens)
- Day 19: `cron` (/etc/cron.d/), reading cron scripts, `/tmp/` lockers
- Day 20: `md5sum` (hashing), `cut -d ' ' -f 1` (grab first field), `echo`

### Script Creation & Exploitation
- Day 21: `nano` (text editor to create files), `cp` (copy files)
- Day 21: Creating shell scripts (`.sh` files)
- Day 21: `/var/spool/` (drop box folders for cron jobs)
- Day 21: Writing custom scripts and dropping them for robots to execute
- Day 21: Privilege Escalation (using a lower account to gain higher access)
- Day 24: Escaping restricted shells (Pausing `more` -> pressing `v` -> opening `vi` editor -> `:set shell=/bin/bash` -> `:shell`)
- Day 24: Bypassing `localhost` firewall blocks by routing connections externally from your own PC
- Day 25: SUID binaries and the Golden Formula: `[Hidden Tool] + [Command] + [Secret File] = Privilege Escalation`

### Brute Force & Looping
- Day 23: `for` loops in Bash (`do` starts loop body, `done` ends it)
- Day 23: Brute Force attacks (trying every possible combination)
- Day 23: Piping loop output into netcat (`| nc localhost PORT`)
- Day 23: `printf "%05d"` (zero-padding numbers to fixed width)

### Redirection & Pipes
- Day 18: `>` (overwrite), `<` (feed file in), `|` (pipe), `>>` (append without deleting)

---

## 🐍 PYTHON

### Basics
- Day 5: `print()`, variables
- Day 7: f-strings (`f"..."`), strings
- Day 9: `if / else`
- Day 10: `for` loops, `range()`
- Day 25: Building a Port Scanner (combining Lists `[ ]`, `for` loops, and `if/elif` logic to scan multiple targets)

### Data Structures
- Day 11: Lists `[ ]`, indexing `[0]`
- Day 16: `.split()`, `.join()`, `.replace()`
- Day 20: `in` keyword (membership check), `[ ]` List vs `( )` Tuple
- Day 21: Dictionaries `{ }` (key-value pairs)
- Day 21: Accessing dictionary values with `dict["key"]`
- Day 21: `==` (equality comparison) vs `in` (membership check)

### Functions & Tools
- Day 23: `def` (define a function / create a reusable tool)
- Day 23: Calling a function `func()` vs Assigning a variable `func = ()` (which destroys the tool)
- Day 23: `and` keyword (check BOTH conditions are true)
- Day 23: DRY Principle (Don't Repeat Yourself — build once, call many times)
- Day 24: `print` (shows data to the human screen) vs `return` (hands data back to the script to save in a variable)
- Day 24: Python Indentation (spacing dictates what is *inside* the tool vs what runs in the *main script*)
- Day 25: `elif` (Else-If) to prevent double-triggering in `if` statements (chaining conditions)

### File I/O
- Day 18: `open()`, `"r"` (read), `"w"` (write), `with` (safe close), `.readlines()`
- Day 19: `\n` (new line = Enter key)

---

## 🌐 CCNA (NetworkChuck)

- Day 3: Ep 1 (Networking intro)
- Day 12: Ep 2
- Day 19: Ep 3 (Switches, MAC addresses, Flooding, Layer 2)
- Day 21: Ep 4 (OSI Layers: Layer 7 App, Layer 4 Transport, Layer 3 IP/Router, Layer 2 MAC/Switch)
- Day 23: Ep 4 Deep Dive (Encapsulation: adding headers as data moves DOWN the OSI model. Decapsulation: removing headers as data moves UP)
- Day 23: Ep 5 (TCP 3-Way Handshake: SYN → SYN-ACK → ACK)
- Day 23: Ep 5 (TCP = reliable with handshake, UDP = fast without handshake)
- Day 23: Ep 5 (Ports: HTTP = 80, HTTPS = 443)
- Day 24: Ep 6 (3-Tier Network Architecture: Access Layer (Tier 1 - end devices), Distribution Layer (Tier 2 - middle management), Core Layer (Tier 3 - high-speed backbone))
- Day 25: Ep 6 Data Centers (Spine-Leaf architecture vs 3-Tier. Spine-Leaf guarantees exactly 2 hops for ultra-fast East-West server traffic).

---

## 🔥 CYBERSECURITY CONCEPTS

- Day 23: Hashing vs Encryption vs Encoding
  - Encoding (Base64): Translation only. No security. Anyone can decode it.
  - Encryption (AES-256): Two-way locked box. Reversible ONLY with the key.
  - Hashing (SHA-256 / MD5): One-way shredder. Irreversible. Cannot be "decrypted."
- Day 23: Dictionary Attack (using a wordlist like RockYou.txt to crack hashes)
- Day 23: Brute Force Attack (trying EVERY possible combination)
- Day 23: Avalanche Effect (changing ONE character completely changes the entire hash)
- Day 23: Salting (adding random characters to passwords before hashing to defeat dictionary attacks)
- Day 24: Asymmetric Encryption (Public Key = The Padlock you share with the world. Private Key = The Physical Key you keep safe to unlock it)
- Day 24: SSH Fingerprints / Host Keys (Verifying the server's identity to prevent Man-in-the-Middle fake server attacks)
- Day 25: The CIA Triad (Confidentiality = secrecy, Integrity = unaltered data, Availability = system uptime)

---

## 🧠 MINDSET & HABITS

- Day 18: Understanding-Creation Gap (reading vs writing code)
- Day 19: Tutorial Hell (copying vs understanding), breaking out of it
- Day 20: Case Sensitivity (i vs I), Spaced Repetition, Dangerous Hacker Roadmap, Home Lab plan
- Day 21: Thinking process over memorization (WHY before WHAT)
- Day 21: Privilege Escalation is the #1 concept in hacking
- Day 23: Debugging mindset (finding the 1-character bug that breaks everything)
- Day 23: Never do manually what a machine can do automatically
- Day 24: Environment Debugging (Diagnosing infrastructure/OS blocks, like Windows CMD height limits, instead of blaming the tool)
- Day 24: The "No Quit" Hacker Mindset (Pivoting strategies when the front door is blocked)
- Day 25: System Auditing (Catching missing components, like spaced repetition, and holding the system accountable)

---

## 📌 HOW TO USE THIS FILE
1. Every new day, add the new concepts to the right section.
2. The daily quiz (Section 3) pulls random questions from this entire list.
3. If I get a question wrong, it goes back into rotation until I master it.
