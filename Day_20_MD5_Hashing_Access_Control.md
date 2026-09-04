# Day 20: MD5 Hashing, Case Sensitivity & Access Control
**Date:** September 05, 2026

## 🐧 OverTheWire: Level 22 -> 23

### The Challenge: The MD5 Shredder
**The Concept:** `md5sum` is a mathematical shredder. It turns any sentence into a unique barcode (hash). The same sentence always produces the same barcode, but even ONE different letter creates a completely different barcode.

**The Hack:**
The cron script hashed the sentence "I am user bandit22" to create a secret filename in `/tmp/`. We bypassed the robot by manually running the same `md5sum` command but feeding it "I am user **bandit23**" to calculate our own barcode.

**Commands Used:**

### ⚠️ The Ultimate Lesson: Case Sensitivity
I spent time debugging because I used a **lowercase `i`** instead of a **capital `I`**.

- `echo i am user bandit23` = WRONG barcode
- `echo I am user bandit23` = CORRECT barcode

**Takeaway:** Computers are ruthlessly literal. They do exactly what you type, not what you mean. `i` and `I` are completely different to Linux. Attention to detail is the #1 skill of a hacker.

---

## 💻 Code From Scratch: The Python Bouncer

### The Mission
Build an access control system from scratch. No copying. No tutorial hell.

### The Code
```python
print("----- PYTHON BOUNCER -----")

vip_list = ["neo", "trinity", "morpheus"]
guest = "neo"

if guest in vip_list:
    print("\naccess granted.")
else:
    print("\naccess denied.")
