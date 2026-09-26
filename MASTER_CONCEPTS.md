# MASTER CONCEPTS LOG (Day 1 to Day 40)
*This is my long-term memory bank. The daily quiz pulls from this list.*

> **INSTRUCTION FOR AI:** 
> Read this entire file carefully. This is the student's complete knowledge base from Day 1 to Day 40. Do not repeat topics already covered. Use this to generate daily quizzes, track progress, and continue the curriculum exactly where we left off.

*NOTE: Days 1-17 are reconstructed. Adjust day numbers to match my real journey.*
*NOTE: Day 22 was skipped (busy day). No concepts added.*
*NOTE: Day 35 was skipped (rest day). No concepts added.*
*NOTE: Day 39 was skipped (rest/lost day). No concepts added.*

---

## 🐧 LINUX (OverTheWire Bandit)

### Navigation & Reading
- Day 1: `ssh` (connect to server), `cat` (read file), `pwd` (where am I)
- Day 2: `ls` (list files), `cd` (change directory), spaces in filenames (`cat "my file.txt"`)
- Day 3: Hidden files (`ls -a`), `cd ..` (go up)

### Searching & Filtering
- Day 4: `find` (locate files), `find -type f` (find only files, ignore folders), `find -size`
- Day 5: `grep` (search text), `grep -v` (invert match - show everything EXCEPT the search term), `sort`, `uniq`
- Day 6: `strings` (read text from binary), `base64` (decode)
- Day 7: `tr` (translate/decode rot13), `xxd` / `hexdump` (read hex)
- Day 36: `sort | uniq -u` (find the ONLY line that appears once in a file)

### Archives & Compression
- Day 8: `tar`, `gzip`, `bzip2` (extract archives)
- Day 40: The Compression Maze (Bandit 12: reversing hexdumps with `xxd -r`, then using `file` to detect and peel back multiple layers of gzip, bzip2, and tar archives)

### Networking & Permissions
- Day 9: `ssh` keys (passwordless login)
- Day 10: `nc` / netcat (talk to ports), connecting to ports
- Day 11: `nmap` (scan ports), SSL connections
- Day 12: `diff` (compare files)
- Day 13: SUID, `chmod` (permissions), `bandit20-do`
- Day 24: `scp` (Secure Copy) to exfiltrate files securely without corrupting Linux `\n` line endings
- Day 24: `icacls` (Windows command to lock down SSH key permissions, equivalent to `chmod 600`)
- Day 34: Daily Grind Methodology (Replaying random Bandit levels blind to build permanent muscle memory)
- Day 36: `openssl s_client` (connect to SSL/TLS ports manually, type password into encrypted tunnel)
- Day 36: `cron` job exploitation (reading `/etc/cron.d/` scripts, finding where robots dump secrets in `/tmp/`)
- Day 37: `nmap -sV localhost -p RANGE` (Service Version detection to identify SSL vs plain-text ports)
- Day 37: SSH Private Key extraction via SSL tunnel (server hands you RSA key instead of password)
- Day 37: `chmod 600` on SSH keys (SSH rejects keys with open permissions)
- Day 37: `ssh -i /path/to/key user@host` (login with keycard instead of spoken password)
- Day 37: `scp -P 2220 user@host:/remote/path D:\local\path` (exfiltrate files from server to Windows laptop)
- Day 37: Internal vs External SSH (using `localhost` when already inside the server vs `-p 2220` from outside)
- Day 38: SSH Command Execution Bypass (Appending a command to the SSH string like `ssh user@host "cat readme"` executes it during the handshake before instant-disconnect scripts can kick you out)
- Day 38: SUID Binary Exploitation (Using `./bandit20-do cat /etc/bandit_pass/bandit20` to force a SUID binary to run `cat` with the privileges of the binary's owner)
- Day 40: The Kata Speedrun Protocol (Re-solving levels 0-12 blind, with zero AI hints, using only `man` pages and `--help` to build unbreakable muscle memory)

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
- Day 37: Piping passwords directly into SSL tunnels (`cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:PORT -quiet`) to eliminate human copy-paste errors

### Version Control & Exfiltration
- Day 27: `git clone` (steals project and hidden `.git` history) vs `scp` (moves files without history)
- Day 27: Linux Flag Rule (Flags eat the very next word. E.g., `scp -i [key] -P [port]`)
- Day 27: `rm -rf` (Recursive Force delete. Nukes folders instantly without confirmation)
- Day 29: `git branch -a` (reveals ALL branches including hidden remote branches)
- Day 29: `git checkout remotes/origin/dev` (teleports workspace into hidden branch)
- Day 29: Red (`-`) = deleted, Green (`+`) = added in Git diff output
- Day 30: `git tag` (reveals ALL bookmarks/tags in the repository)
- Day 30: `git show [tagname]` (reads content inside a specific tag)
- Day 30: Tags vs Branches vs Stashes (Tags = bookmarks, Branches = parallel timelines, Stashes = temporary drawers)
- Day 36: `git clone` speed-run (clone repo, `cd repo`, `cat README` to find password in plain sight)

---

## 🕸️ WEB HACKING (OverTheWire Natas)

### Reconnaissance & Information Disclosure
- Day 34: View Page Source (CTRL+U) to reveal hidden HTML, comments, and secrets
- Day 34: Information Disclosure (Developers leaking secrets in HTML comments, directory listings, or config files)
- Day 34: Directory Listing (Browsing a folder URL directly to see all files when index.html is missing)
- Day 34: robots.txt (File that tells search engines what to hide — hands hackers a map to secret directories)
- Day 36: Source Code Disclosure via PHP `include` (Natas 6: `include "includes/secret.inc"` leaks the secret file path)
- Day 36: Browsing directly to `.inc` files (Server serves raw code instead of executing it because it's not `.php`)

### Bypassing Client-Side Restrictions
- Day 34: Client-side restrictions are NOT security (Blocking right-click is a suggestion, not a control)
- Day 34: Bypassing right-click blocks with keyboard shortcuts (CTRL+U) or view-source: URL prefix

### HTTP Headers & Session Forgery
- Day 34: HTTP Referer header (Tells the server where you came from. Forgeable with curl -e)
- Day 34: HTTP Cookies (Client-side "wristbands" the server trusts. Forgeable with curl -b)
- Day 34: Session Forgery (Editing a cookie value like loggedin=0 to loggedin=1 to impersonate an admin)
- Day 34: HTTP Status Code 401 (Unauthorized = wrong credentials)

### Path Traversal & File Inclusion
- Day 36: Path Traversal / Directory Traversal (Using `../` to escape web directory and read system files)
- Day 36: URL manipulation (`?page=home` → `?page=../../../../etc/natas_webpass/natas8`)
- Day 36: `../` means "go up one directory" — chain multiple to reach root `/`

### Encoding & Obfuscation Reversal
- Day 36: Reversing PHP encoding chains (`bin2hex(strrev(base64_encode($secret)))`)
- Day 36: Decoding pipeline: `xxd -r -p` (hex→text) → `rev` (reverse) → `base64 -d` (decode)
- Day 36: Piping decode chains in Bash (`echo "HEX" | xxd -r -p | rev | base64 -d`)

### Command Injection & Regex Bypasses
- Day 38: Command Injection (Natas 9: Using the semicolon `;` as a "Stop Sign" to end the developer's `grep` command and chain your own `cat` command)
- Day 38: The Comment Mute Button (Using `#` at the end of a payload to comment out leftover garbage text the PHP script blindly appends)
- Day 38: Regex Bypass / Abusing Tools (Natas 10: When `;` and `|` are blocked, tricking `grep` into reading the password file by passing a blank search `""` followed by the target file path)
- Day 38: Natas 0-10 Speedrun (Building muscle memory by repeating early levels daily without hints)

### Cryptography & Cookie Forgery
- Day 40: XOR Encryption (Natas 11: Server encrypts session cookies using a repeating XOR key)
- Day 40: The XOR Magic Formula: `A ⊕ B = C` (Plain-text ⊕ Key = Cipher-text) and `A ⊕ C = B` (Plain-text ⊕ Cipher-text = Secret Key)
- Day 40: Reversing XOR to steal the key (XORing the known default JSON with the Base64-decoded cookie reveals the secret key)
- Day 40: Forging Encrypted Cookies (Modifying the JSON to `"showpassword":"yes"`, XORing it with the stolen key, and Base64 encoding it to bypass the lock)
- Day 40: Base64 Padding Errors (URL-encoded cookies use `%3D` instead of `=`, which breaks Python's `b64decode` until manually fixed)
- Day 40: Python 3 Bytes vs Strings (`b64decode` returns raw bytes, so you don't need `ord()` on the cipher-text, only on the plain-text string)
- Day 40: CyberChef (Visual drag-and-drop crypto tool used by real pentesters to avoid writing custom Python scripts for quick math)

### curl Flags for Web Hacking
- Day 34: curl -u user:pass (Basic Authentication)
- Day 34: curl -e "URL" (Forge the Referer header)
- Day 34: curl -b "name=value" (Send a forged cookie)

---

## 🐍 PYTHON

### Basics
- Day 5: `print()`, variables
- Day 7: f-strings (`f"..."`), strings
- Day 9: `if / else`
- Day 10: `for` loops, `range()`
- Day 25: Building a Port Scanner (combining Lists `[ ]`, `for` loops, and `if/elif` logic to scan multiple targets)
- Day 36: `input()` (asks user to type something and stores it in a variable)
- Day 36: `=` (ASSIGNMENT: stores a value) vs `==` (COMPARISON: checks if equal)
- Day 36: `if/else` access control logic (comparing user input to a secret password)

### Data Structures
- Day 11: Lists `[ ]`, indexing `[0]`
- Day 16: `.split()`, `.join()`, `.replace()`
- Day 20: `in` keyword (membership check), `[ ]` List vs `( )` Tuple
- Day 21: Dictionaries `{ }` (key-value pairs)
- Day 21: Accessing dictionary values with `dict["key"]`
- Day 21: `==` (equality comparison) vs `in` (membership check)
- Day 34: Tuples `( )` for auth credentials (Immutable — username and password can't change mid-flight)
- Day 34: Dictionaries `{ }` for cookies (key:value pairs like `{'loggedin': '1'}`)
- Day 37: Lists `[ ]` (Hacker's toolbelt — stores multiple targets in one variable)
- Day 37: Zero-based indexing (slot 0 = first item, slot 1 = second, slot 2 = third)
- Day 37: Square brackets `[ ]` = List (mutable) vs no brackets / `( )` = Tuple (immutable)

### Loops & Automation
- Day 38: `for` loops (The Conveyor Belt: iterating through Lists automatically without hardcoding indexes)
- Day 38: Python Indentation (The 4-space rule that dictates exactly what code is *inside* the loop vs outside)
- Day 38: Protecting built-in tools (Never use `str`, `print`, `list` as variable names, or you destroy the built-in function and cause TypeErrors)
- Day 40: The Indentation Golden Rule (Misaligning a `try:` block with a `for` loop causes the loop to only execute once instead of iterating)

### Functions & Tools
- Day 23: `def` (define a function / create a reusable tool)
- Day 23: Calling a function `func()` vs Assigning a variable `func = ()` (which destroys the tool)
- Day 23: `and` keyword (check BOTH conditions are true)
- Day 23: DRY Principle (Don't Repeat Yourself — build once, call many times)
- Day 24: `print` (shows data to the human screen) vs `return` (hands data back to the script to save in a variable)
- Day 24: Python Indentation (spacing dictates what is *inside* the tool vs what runs in the *main script*)
- Day 25: `elif` (Else-If) to prevent double-triggering in `if` statements (chaining conditions)
- Day 34: `import requests` (Load the web-hacking library to send HTTP requests from Python)
- Day 34: `requests.get(url)` (Sends an HTTP GET request — same as typing a URL and hitting Enter)
- Day 34: `response.text` (Prints the raw HTML string instead of the Python object)

### Network Programming (Sockets)
- Day 40: `import socket` (Loading Python's built-in networking toolbox)
- Day 40: `s = socket.socket()` (Creating a blank network handshake object)
- Day 40: `s.connect(("IP", Port))` (Dialing a specific IP and Port to check if it's open)
- Day 40: `s.settimeout(1)` (Preventing the script from hanging for 60 seconds on closed ports by forcing a 1-second timeout)
- Day 40: `try:` and `except:` blocks (The safety net that catches connection errors on closed ports so the script doesn't crash)
- Day 40: `AttributeError` debugging (Catching typos like `socket.scoket()` by reading Python's exact error trace)

### File I/O
- Day 18: `open()`, `"r"` (read), `"w"` (write), `with` (safe close), `.readlines()`
- Day 19: `\n` (new line = Enter key)
- Day 29: `.strip()` (removes hidden `\n` newline character from file lines)
- Day 29: `break` (stops a loop immediately when a condition is met)

### User Input & Comparison
- Day 30: `input()` (asks user to type something and stores it in a variable)
- Day 30: `=` (ASSIGNMENT: stores a value) vs `==` (COMPARISON: checks if equal)
- Day 30: Comparing TWO DIFFERENT variables (user_guess vs correct_password) instead of comparing a variable to itself

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
- Day 27: WAN & Metro Ethernet (Connecting LANs across long distances and metropolitan areas).
- Day 27: MPLS (Multiprotocol Label Switching - high-speed routing using labels instead of IP addresses).
- Day 27: E-LAN (Multipoint-to-multipoint mesh) vs E-Tree (Hub-and-Spoke routing).
- Day 36: IPv4 Addressing (4 octets, 32 bits total, each octet 0-255)
- Day 36: Subnet Masks (255.255.255.0 = first 3 octets are Network ID, last octet is Host ID)
- Day 36: Network ID vs Host ID (Street name vs House number)
- Day 37: Ep 9 (SOHO Home Router = 4-in-1 device: Router + Switch + WAP + Firewall/NAT)
- Day 37: NAT (Network Address Translation — translates private IPs to single Public IP for internet access)
- Day 37: DHCP (Dynamic Host Configuration Protocol — automatically hands out IP addresses to devices)
- Day 37: Private IP ranges (192.168.x.x, 10.x.x.x, 172.16-31.x.x) vs Public IPs
- Day 37: LAN ports on home router act as Layer 2 Switch internally
- Day 38: ARP (Address Resolution Protocol - maps Layer 3 IP addresses to Layer 2 MAC addresses by shouting "WHO HAS THIS IP?")
- Day 38: ARP Spoofing / Poisoning (Lying to both the Router and the Victim about your MAC address to intercept local Wi-Fi traffic)
- Day 38: Man-in-the-Middle (MitM) Attack (Sitting perfectly in the middle of the wire on a local Wi-Fi to read unencrypted data)
- Day 40: DNS (Domain Name System - The internet's phonebook that translates human domain names into machine IP addresses)
- Day 40: DNS Spoofing / DNS Poisoning (Intercepting a victim's DNS request and lying about the IP address to redirect them to a hacker's fake website)
- Day 40: ARP vs DNS Spoofing (ARP lies about MAC addresses on the local LAN; DNS lies about Domain Names for internet routing)

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
- Day 27: The AAA Framework (Authentication = Who are you? | Authorization = What can you do? | Accounting = What did you do?)
- Day 29: Broken Access Control (When a system fails at Authorization)
- Day 29: IDOR (Insecure Direct Object Reference - changing an ID in a URL to access another user's data)
- Day 29: Privilege Escalation via Access Control (Changing `role=user` to `role=admin` in cookies/parameters)
- Day 34: The Client Trust Problem (Servers trust cookies, headers, and IDs sent by the client. Attackers forge them)
- Day 34: Cloud IP Blocking (OverTheWire blocks Google Cloud/AWS IPs. Exploits must run from residential IPs — a real-world firewall behavior)
- Day 34: Never push secrets to GitHub (Real passwords/SSH keys get stolen by bots. Use <REDACTED> placeholders)
- Day 36: SQL Injection (SQLi) — The Database Killer
  - Payload: `' OR 1=1 --`
  - `'` closes the string early (break out of the jail)
  - `OR 1=1` is always TRUE (bypasses logic check)
  - `--` comments out everything after it (deletes the password check)
- Day 37: OWASP Top 10 (The 10 most dangerous web vulnerabilities)
- Day 37: Broken Access Control = OWASP #1 (Checking permissions at login but NOT on subsequent page loads)
- Day 37: IDOR via URL manipulation (Changing `user_id=100` to `user_id=1` to access admin data)
- Day 37: The VIP Room Analogy (Bouncer checks ID at front door but not at VIP room door)
- Day 37: Fix: Check permissions on EVERY page load, not just at login
- Day 38: Cross-Site Scripting (XSS) (Injecting malicious JavaScript via `<script>` tags to hack the *User's Browser*, unlike Command Injection which hacks the *Server's Terminal*)
- Day 38: The Poisoned Megaphone (Websites blindly pasting user input directly into HTML, allowing browsers to execute attacker-controlled scripts)
- Day 40: SQLi Anatomy Deep Dive (Understanding exactly why the Logic Bomb works: The single quote breaks the container, the math forces a TRUE condition, and the double-dash silences the syntax error)

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
- Day 30: Writing code from scratch (building line by line instead of copying)
- Day 34: Rest is a weapon (Pushing through exhaustion causes burnout. Strategic rest protects the mission)
- Day 34: The No-Quit discipline (Feeling the burn but refusing to fold — then resting with purpose)
- Day 34: Demanding accountability (Asking the mentor to teach from scratch and NEVER give the full code)
- Day 36: Hacker Fatigue is real (Solving a puzzle once doesn't mean you retain it forever. Context-switching dumps memory. Re-learning is normal.)
- Day 36: The GPS Analogy (You can drive to a destination with GPS, but driving from memory the next day feels impossible. That doesn't mean you can't drive.)
- Day 37: Machine-to-Machine piping (Never copy-paste passwords manually. Use `cat /etc/bandit_pass/level | command` to eliminate human error)
- Day 37: Adapt your attack path (If localhost blocks you, pivot to your laptop. If terminal is confusing, use Notepad. The goal is the same.)
- Day 38: The Night Shift Protocol (Reclaiming a "wasted" day by executing a massive, focused grind late at night instead of giving up)
- Day 38: The 40-Question Gauntlet (Testing raw recall under extreme sleep deprivation to force the brain to lock data into long-term memory)
- Day 40: The Redemption Grind (Using guilt over a skipped day to fuel a massive, high-intensity study session instead of quitting)
- Day 40: Self-Auditing (Honestly admitting when a speedrun took 2 hours and used hints, rather than faking a 30-minute time. Real hackers audit themselves.)
- Day 40: Micro-stepping (Breaking down overwhelming coding tasks into single-line instructions to build confidence and bypass mental blocks)
- Day 40: Tool Builder vs. Tool User (Understanding *how* tools like Nmap work at the socket level so you can build custom evasion tools instead of just pressing buttons)
- Day 40: The "Discover, Don't Copy" Protocol (Demanding to write code from scratch and figure out the logic, rather than just filling in blanks provided by AI)

---

## 📌 HOW TO USE THIS FILE
1. Every new day, add the new concepts to the right section.
2. The daily quiz (Section 3) pulls random questions from this entire list.
3. If I get a question wrong, it goes back into rotation until I master it.
4. Paste this file at the start of any new AI session to restore full memory.
