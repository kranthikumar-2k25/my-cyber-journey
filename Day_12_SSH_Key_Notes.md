# Day 12: Beating the SSH Key Boss (Level 13 -> 14)
**Date:** August 27, 2026

## 🎯 The Challenge
I was given an SSH private key instead of a password. I had to figure out how to use it to log into Level 14.

## 🧠 The 5 Things I Learned
1. **The Localhost Block:** You cannot SSH from a server into itself. OverTheWire blocks localhost connections to save resources. You must bring the key to your local machine.
2. **Secure Copy (`scp`):** Copying/pasting crypto keys into Notepad breaks them because of hidden formatting characters. `scp` transfers raw bytes safely.
   - Command: `scp -P 2220 user@host:remote_file local_path`
   - *Pro Tip: `scp` uses capital `-P` for port, while `ssh` uses lowercase `-p`.*
3. **The `.txt` Trap:** Windows hides file extensions. Notepad secretly saves files as `.txt`, which breaks SSH paths.
4. **Strict Permissions:** SSH refuses to use a private key if it is readable by other users. 
5. **Locking Down Files:** I used `icacls` to remove inherited permissions and grant Read-only access to my specific user.
   - `icacls file /inheritance:r`
   - `icacls file /grant:r "%USERNAME%:R"`

## 🚀 Final Command
`ssh -i D:\newkey.private bandit14@bandit.labs.overthewire.org -p 2220`

## 💡 Mindset Shift
I felt like I learned nothing because I was in "survival mode" fixing errors. But looking back, I mastered file permissions, secure transfers, and SSH authentication. Following instructions builds muscle memory. The concepts stick when you review them.
