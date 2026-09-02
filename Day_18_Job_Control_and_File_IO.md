# Day 18: Job Control, Cron Jobs & Python File I/O
**Date:** September 03, 2026

## 🐧 OverTheWire: Level 20 -> 21 -> 22

### Level 20: Background Processes & Terminal Multiplexing
**Concepts Learned:**
1. **Job Control:** Paused a program with `CTRL-Z`, pushed it to background with `bg`.
2. **The `&` Symbol:** Runs a command silently in the background.
3. **`tmux`:** Split the terminal into multiple panes using `CTRL-B` and `"`. A real-world superpower.

### Level 21: Cron Jobs (The Invisible Worker)
**Concept:** `cron` is Linux's alarm clock. It runs scripts automatically on a schedule.
**The Hack:** Found the cron script in `/etc/cron.d/`, read it, and stole the password it saved in `/tmp/`.

## 🐍 Python: File I/O & Script Building

### File I/O
| Python | Linux Equivalent |
| :--- | :--- |
| `open("file", "w")` | `echo "text" > file` |
| `open("file", "r")` | `cat file` |
| `.readlines()` | Reads file into a List |

**Key Rule:** You must CREATE a variable before using it in an f-string. Forgetting this causes a `NameError`.

### The Understanding-Creation Gap
Today I learned that reading code and writing code use different parts of the brain. I practiced bridging the gap by building scripts from scratch.

**Skills Practiced:**
- Creating Lists: `passwords = ["kickass", "kickme", "kickyour"]`
- Loops: `for x in passwords:`
- Conditions: `if x == "kickme":`
- Splitting Strings: `giant_string.split(", ")`

**The Golden Rule:** Quotes make it a literal string. No quotes means it is a variable.
