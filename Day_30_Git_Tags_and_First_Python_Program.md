# Day 30: Git Tags & My First Python Program
**Date:** September 14, 2026

## 🐧 OverTheWire: Level 30 -> 31

### The Challenge: The Hidden Bookmark
**The Concept:** Level 30 gives you a Git repository where the developer hid the password in a **Git Tag**. Tags are bookmarks that point to specific commits. They don't show up in `git log`, `git branch -a`, or `git stash list`.
**The Hack:** Used `git tag` to reveal all bookmarks, then used `git show secret` to read the content inside the hidden tag.

**Key Commands:**
- `git tag` (reveals ALL bookmarks/tags in the repository)
- `git show [tag_name]` (reads the content inside a specific tag)

### The Big Lesson: Tags vs Branches vs Stashes
| Git Feature | What it does | Where to find it |
|---|---|---|
| **Branch** | Parallel timeline (alternate universe) | `git branch -a` |
| **Stash** | Temporary secret drawer (uncommitted code) | `git stash list` |
| **Tag** | Bookmark pointing to a specific commit | `git tag` |

Developers use tags to mark version releases (`v1.0`, `v2.0`). Hackers use tags to find secrets the developer forgot to delete.

---

## 🐍 Python: My First Program From Scratch

### The Concept
For the first time, I wrote a complete Python program WITHOUT copying code. I built it line by line, understanding what each piece does.

### The Code I Wrote
```python
correct_password = "hacker123"
user_guess = input("what is the password: ")

if user_guess == correct_password:
    print("access granted")
else:
    print("access denied")
