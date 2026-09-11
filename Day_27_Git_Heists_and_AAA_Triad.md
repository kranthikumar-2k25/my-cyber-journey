# Day 27: Git Heists, SCP vs Git, & The AAA Triad
**Date:** September 12, 2026

## 🐧 OverTheWire: Level 27 -> 28

### The Challenge: The Developer's Mistake
**The Concept:** Level 27 gives you a Git repository URL instead of a normal file. Git is a developer's time machine. It tracks every single edit, deletion, and mistake ever made to the code.
**The Hack:** Used `git clone` to download the repository AND its hidden `.git` history database to a local machine. Developers often delete hardcoded passwords from files, but forget they are permanently frozen in the Git history.

**Key Commands:**
- `git clone ssh://user@host:2220/path/to/repo` (Steals the project and its history)
- `ls -la` (Reveals the hidden `.git` database folder)
- `rm -rf repo` (The "Wipe Command" to force-delete the directory and hidden files)

### The Big Lesson: Tool Selection (`scp` vs `git`)
| Tool | What it actually does | Best used for |
|---|---|---|
| **`scp`** | Secure Copy. Acts like a moving truck. | Stealing single files (`/etc/passwd`), SSH keys, or configs. |
| **`git clone`** | Steals project + hidden history. | Stealing source code to dig through deleted passwords/commits. |

### Linux Flag Rule: "Flags Eat The Next Word"
When writing commands, order matters. A flag immediately consumes the next word as its instruction.
- **With Key:** `scp -i D:\mykey.ssh -P 2220 user@host:/file D:\`
- **Without Key:** `scp -P 2220 user@host:/file D:\`
*(If you put `-P 2220` right after `-i`, Linux thinks your key file is literally named "-P" and crashes).*

---

## 🔥 Cybersecurity: The AAA Framework

Every security system in the world is built on these three pillars. If you know which "A" you are attacking, you know how to beat it.

| The "A" | Definition | Hacker Translation | Real-World Example |
|---|---|---|---|
| **Authentication** | Who are you? | Proving your identity. | Typing a password or using an SSH Key. |
| **Authorization** | What are you allowed to do? | Checking your permissions. | The `bandit27-do` SUID file (Privilege Escalation). |
| **Accounting** | What did you do? | Tracking your actions. | The `.git` history or server login logs. |

---

## 🌐 CCNA: WAN, MPLS, & Metro Ethernet

### Connecting the Cities (Wide Area Networks)
When a company has offices in different cities, Local Area Networks (LANs) aren't enough. They need massive infrastructure to connect them.

| Concept | Purpose | Hacker Perspective |
|---|---|---|
| **WAN** | Connects local networks (LANs) across long distances. | The inter-city highway. If you compromise a WAN link, you intercept traffic between company branches. |
| **MPLS** | High-speed routing using "labels" instead of IP addresses. | The VIP express lane. Extremely fast and heavily routed. Critical corporate traffic lives here. |
| **Metro Ethernet** | High-speed Ethernet networks covering a metropolitan area. | The city ring road connecting corporate offices in the same city. |
| **E-LAN** | Multipoint-to-multipoint (Full Mesh). | All branches can talk directly to each other over the Metro. |
| **E-Tree** | Rooted multipoint (Hub-and-Spoke). | The HQ (Root) talks to branches (Leaves), but branches cannot talk to each other. |
