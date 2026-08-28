# Day 13: Python Log Analyzer
# Date: August 28, 2026
# 
# WHY THIS MATTERS IN THE REAL WORLD:
# When you hack a server or defend a network, the logs look like long, messy sentences.
# This script uses .split() to chop the sentence into a list and index numbers
# to extract specific data (like usernames and attacker IP addresses).
# This is the exact foundation of Intrusion Detection Systems (IDS).

print("--- PYTHON LOG ANALYZER ---")

# A messy server log captured from a network
log = "Failed password for bandit14 from 192.168.1.50 port 22"

# .split() looks for spaces and chops the string into a list of words
words = log.split()

# Python starts counting at ZERO.
# Index 0 = 'Failed'
# Index 1 = 'password'
# Index 2 = 'for'
# Index 3 = 'bandit14'
# Index 4 = 'from'
# Index 5 = '192.168.1.50'
# Index 6 = 'port'
# Index 7 = '22'

# Extract specific data using index numbers
username = words[3]
ip_address = words[5]

# Print the extracted data cleanly
print("Full Log:", log)
print("Target Username:", username)
print("Attacker IP Address:", ip_address)

# OUTPUT:
# Full Log: Failed password for bandit14 from 192.168.1.50 port 22
# Target Username: bandit14
# Attacker IP Address: 192.168.1.50
