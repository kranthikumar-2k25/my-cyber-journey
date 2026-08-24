# Day 9: Cryptography & Decoding (ROT13)
**Date:** August 24, 2026

## 🎯 Today's Focus
Today was about cryptography. I learned how the ROT13 cipher works and solved it using two different tools: Linux and Python.

## 🐧 OverTheWire: Level 11 -> Level 12
**The Challenge:** The password is stored in `data.txt`, but every letter has been "rotated by 13 positions" (the ROT13 cipher).
**The Concept:** The alphabet is a circle. If you shift A by 13, you get N. If you shift N by 13, you wrap around and get A.
**The Solution:** I used the `tr` (translate) command to map the normal alphabet to the shifted alphabet.
**Command Used:** 
```bash
cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
```
**Key Learning:** `tr` maps characters position-by-position. `n-za-m` is shorthand for the shifted alphabet (n-z followed by a-m).

## 🐍 Python: The ROT13 Decoder
I recreated the same decode in Python using a built-in library.
**Code:**
```python
import codecs

message = "gurl nernq gur cnffjbeq"
secret = codecs.decode(message, 'rot_13')
print("Decoded Message:", secret)
```
**Key Concepts:**
- `import codecs`: Brings in Python's built-in "toolbox" for handling encodings.
- `codecs.decode(message, 'rot_13')`: Uses the built-in ROT13 key to unlock the text instantly.
- **Big Picture:** Instead of writing a loop to shift letters manually, Python's libraries give you pre-built tools.

## 🧠 Mindset
I felt like I "wasted the day" because I only did two things. But I learned that doing *something* focused is better than doing *nothing* perfectly. Mastering one deep concept (ROT13) across two environments (Linux + Python) is a real win.
