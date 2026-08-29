# Day 14: Python f-strings and Splitting by Specific Characters
# Date: August 28, 2026
#
# WHY THIS MATTERS IN THE REAL WORLD:
# Server configs, database leaks, and CSV files don't always use spaces.
# They often use colons (:) or commas (,) to separate data.
# We use .split(":") to chop the text at specific characters.
# We use f-strings to dynamically build clean reports from that data.

print("--- PYTHON DATABASE PARSER ---")

# A messy database record where data is separated by colons
record = "bandit16:hunter2_password:admin:192.168.1.99"

# CONCEPT 1: Splitting by a specific character
# We put ":" inside the parentheses to tell Python exactly where to chop.
parts = record.split(":")

print("The full chopped list:", parts)
# Output: ['bandit16', 'hunter2_password', 'admin', '192.168.1.99']

# Extract specific data using index numbers (starting at 0)
username = parts[0]
password = parts[1]
role = parts[2]
ip_address = parts[3]

# CONCEPT 2: f-strings (Formatted Strings)
# The 'f' tells Python: "Look inside the curly braces {} and fill in 
# the blanks with the actual values from my variables."
# Without the 'f', Python would literally print the text "{username}".
# WITH the 'f', Python swaps in the real value.

print(f"ALERT: User {username} logged in.")
print(f"Role: {role}")
print(f"Source IP: {ip_address}")

# OUTPUT:
# ALERT: User bandit16 logged in.
# Role: admin
# Source IP: 192.168.1.99
