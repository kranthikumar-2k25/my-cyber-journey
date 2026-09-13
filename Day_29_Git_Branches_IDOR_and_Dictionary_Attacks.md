# Day 29: Git Branches, IDOR, & Dictionary Attacks
**Date:** September 13, 2026

## 🐧 OverTheWire: Level 28 -> 30

### The Challenge: The Hidden Branches
**The Concept:** Level 29 gives you a Git repository where the developer hid the password in a parallel timeline (branch). The main branch (`master`) says "no passwords in production", but the secret is hiding in `remotes/origin/dev`.
**The Hack:** Used `git branch -a` to reveal ALL branches, then used `git checkout remotes/origin/dev` to teleport into the hidden timeline and steal the password.

**Key Commands:**
- `git branch -a` (reveals ALL branches, including hidden remote branches)
- `git checkout remotes/origin/dev` (teleports your workspace into the hidden branch)
- `git show [commit_id]` (time-travel to see what was deleted in a specific commit)

### The Big Lesson: Parallel Universes in Git
Developers create branches like `dev`, `staging`, `testing` for experimentation. They frequently commit secrets into these branches, scrub them from `master`, but forget to clean up the hidden branches. Hackers clone the repo, switch branches, and steal the secrets.

| Git Concept | What it does | Hacker Perspective |
|---|---|---|
| **`git branch -a`** | Shows all branches (local + remote) | Reveals hidden timelines the developer forgot about |
| **`git checkout`** | Switches your workspace to another branch | Teleports you into the hidden universe to steal secrets |
| **Red (`-`)** | Developer DELETED this | The real password they tried to hide |
| **Green (`+`)** | Developer ADDED this | The replacement text (like `xxx` or `REDACTED`) |

---

## 🔥 Cybersecurity: Broken Access Control (IDOR)

### The Concept: AAA Framework Failure
Every security system is built on Authentication (who you are) and Authorization (what you can do). **Broken Access Control** happens when the system fails at Authorization.

### The Hotel Keycard Analogy
You check into a hotel and get a keycard for Room 201. The hotel **authenticated** you (you are a guest). But what if you walk up to Room 202, swipe your Room 201 keycard, and the door opens? The hotel failed at **Authorization**.

### The Hacker's Favorite Attack: IDOR
**IDOR** (Insecure Direct Object Reference) happens when a web application trusts the user's browser too much.

| Vulnerability | How it works | Real-World Example |
|---|---|---|
| **IDOR** | Changing an ID number in a URL to access another user's data | Changing `account_id=101` to `account_id=102` to download the CEO's bank statement |
| **Privilege Escalation** | A normal user tricking the server into giving Admin rights | Changing `role=user` to `role=admin` in a cookie |

**The Golden Rule:** A server must ALWAYS check permissions on the backend. It must NEVER trust an ID number sent by the client.

---

## 🐍 Python: Dictionary Attack Tool

### The Concept
Hackers don't guess passwords manually. They download massive leaked databases (like `rockyou.txt` with 14 million passwords) and write a Python script to check if the target's password is hiding inside that list.

### The Code
```python
target_password = "secret123"

with open("rockyou.txt", "r") as wordlist:
    passwords = wordlist.readlines()

for word in passwords:
    clean_word = word.strip()  # Removes hidden \n (Enter key)
    
    if clean_word == target_password:
        print(f"🔥 MATCH FOUND! The password is: {clean_word}")
        break  # Stops the loop immediately when match is found
