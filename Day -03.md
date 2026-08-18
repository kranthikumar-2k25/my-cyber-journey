# Day 3: Text Sorting/Uniq in Linux & Python Loops

## 1. Linux Challenges (OverTheWire Bandit 8 → 9)

### Key Concepts Learned:
- **`sort` & `uniq` Pipeline:** Finding the only non-repeated line of text in a massive data file.
- **Why sorting is required:** The `uniq` command only checks adjacent lines, so data must be sorted first.

### Command Used:
```bash
sort data.txt | uniq -u
