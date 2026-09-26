# DAY 40: THE REDEMPTION GRIND 🔥

**Date:** [Today's Date]
**Status:** COMPLETE ✅
**Mindset:** "I wasted Day 39. Today I redeem it."

---

## 🎯 MISSION OBJECTIVE
Redeem the skipped Day 39 with a massive speedrun. No excuses. No quitting.
The goal: Bandit 0-12, Natas 0-11, Python Port Scanner, Cyber Class, CCNA Class, and the 50-Question Mega Quiz.

---

## 🐧 TARGET 1: BANDIT 0-12 SPEEDRUN

### The Gauntlet:
Rebuilt Linux muscle memory from scratch. The goal was to see if my fingers remembered the commands without thinking.

### Levels Cleared:
| Level | Challenge | Weapon Used |
|-------|-----------|-------------|
| 0 | SSH Login | `ssh bandit0@bandit.labs.overthewire.org -p 2220` |
| 1 | File named `-` | `cat ./-` (the `./` stops it from reading it as a flag) |
| 2 | File with spaces | `cat "spaces in this file"` (quotes save your life) |
| 3 | Hidden file | `ls -la` then `cat .hidden` |
| 4 | Human-readable file | `file ./-` then `cat -file0` |
| 5 | Find by size/permissions | `find ./inhere -type f -size 1033c ! -executable` |
| 6 | Find anywhere on server | `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` |
| 7 | Search inside file | `grep millionth data.txt` |
| 8 | Find unique line | `sort data.txt | uniq -u` |
| 9 | Extract from binary | `strings data.txt | grep =` |
| 10 | Base64 decode | `base64 -d data.txt` |
| 11 | ROT13 decode | `cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'` |
| 12 | Hexdump maze | `xxd -r` then `file` to detect compression layers |

### Bandit 12 Deep Dive (The Compression Maze):
```bash
mkdir /tmp/hacker
cp data.txt /tmp/hacker/
cd /tmp/hacker
xxd -r data.txt > output
file output
# Then kept extracting layers:
# gzip -> bzip2 -> tar -> gzip -> tar -> tar -> gzip
