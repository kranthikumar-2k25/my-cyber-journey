print("=== PYTHON SIMULATION OF AWK AND TR ===")

# 1. THE MESSY SERVER REPLY (Contains garbage text and \r ghosts)
messy_reply = "Correct!\r\n-----BEGIN OPENSSH PRIVATE KEY-----\r\nsecret_key_line_1\r\nsecret_key_line_2\r\n-----END OPENSSH PRIVATE KEY-----\r\nDONE"

print("BEFORE (Messy):")
print(messy_reply)
print("-" * 40)

# 2. SIMULATE TR -d '\r' (The Eraser) - Remove invisible \r characters
erased_reply = messy_reply.replace("\r", "")

# 3. SIMULATE AWK (The Scissors) - Cut between BEGIN and END
lines = erased_reply.split("\n")
clean_key = []
inside_key = False # The ON/OFF switch

for line in lines:
    if "-----BEGIN" in line:
        inside_key = True  # Turn switch ON
    
    if inside_key:
        clean_key.append(line)
    
    if "-----END" in line:
        inside_key = False # Turn switch OFF

final_key = "\n".join(clean_key)

print("AFTER (Clean):")
print(final_key)
print("-" * 40)
print("SUCCESS! The key is mathematically perfect.")
