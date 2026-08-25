# Day 10: The Boss Fight & Automation
**Date:** August 25, 2026

## 🎯 Today's Focus
I beat OverTheWire Level 12 (the most tedious "nesting doll" level) and then built a Python script to automate the solution.

## 🐧 OverTheWire: Level 12 -> Level 13
**The Challenge:** A file hidden inside multiple layers of compression (hexdump, gzip, bzip2, tar).
**The Solution:** I learned to use the `file` command to identify hidden file signatures, and chained `xxd`, `gunzip`, `bunzip2`, and `tar` to unpack the data layer by layer.
**Key Learning:** Hackers analyze "Magic Numbers" to identify file types when extensions are missing.

## 🐍 Python: The Automated File Checker
I built a script that mimics the Linux `file` command using string methods.
**Key Concepts:**
- `.endswith()`: Checks if a string ends with a specific pattern.
- `if/elif/else`: Makes decisions based on the file type.
- `for` loops: Automates the check across a list of 5 files in one second.
**Big Picture:** I automated the manual work I did in Linux. That is the hacker mindset.
