# Day 1: Linux Terminal & Bandit Walkthrough

### Commands Mastered:
- `ssh user@host -p port` : Connect to a remote server securely
- `ls -la` : List all files, including hidden (`.`) ones, with details
- `cat filename` : Print file contents to the screen
- `cat ./-` : Read files starting with dashes/special characters
- `file filename` : Check the real file type (human-readable, ASCII, data)
- `find inhere -type f -size 1033c ! -executable` : Search with size/type filters
- `find / -user X -group Y -size 33c 2>/dev/null` : Search whole disk and silence permission errors
