# Day 2: Linux Text Processing & Basic Python Automation

## 1. Linux Challenges (OverTheWire Bandit 7 → 8)

### Key Concepts Learned:
- **Filtering Large Files with `grep`:** Searching for exact keyword matches inside files containing hundreds of thousands of lines.
- **Piping Streams (`|`):** Sending the output of one command as the direct input to another.

### Commands Used:
```bash
# Search for a specific string inside data.txt
grep "millionth" data.txt

# Alternative using piping
cat data.txt | grep "millionth"
