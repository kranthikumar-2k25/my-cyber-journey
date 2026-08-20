# Day 5: Cybersecurity Fundamentals & Python Logic
**Date:** August 18, 2026

## 🎯 Today's Focus
Today was about building foundations. I pushed through a paywall, pivoted back to my core schedule, and combined Linux, Networking theory, and Python scripting.

## 🐧 OverTheWire: Level 8 -> Level 9
**The Challenge:** Find a hidden password in a messy, binary-filled file.
**The Solution:** I used the `strings` command to extract readable text from the garbage, and then piped it into `grep` to search for the `==========` pattern.
**Command Used:** `strings data.txt | grep "=========="`

## 🌐 NetworkChuck: Day 0 - What is Networking?
**Key Takeaway:** A network is simply two or more computers connected together to share resources (files, internet, printers). I also learned the basic difference between IP addresses (logical location) and MAC addresses (physical hardware ID).

## 🐍 Python: Password Checker Script
I built a script that uses `while True` loops, `input()`, and `len()` to validate passwords. 
**Key Concept:** The script keeps asking for a password until the user types one that is at least 8 characters long.
