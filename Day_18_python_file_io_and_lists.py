# ============================================
# DAY 18: PYTHON FILE I/O & SCRIPT BUILDING
# ============================================

# --------------------------------------------
# PART 1: FILE I/O (Writing and Reading)
# --------------------------------------------
print("--- PYTHON FILE MANAGER ---")

# WRITE to a file ("w" mode creates or overwrites)
with open("secret_vault.txt", "w") as vault:
    vault.write("level 21 key:abcdefg\n")
    vault.write("level 22 key:hijklmn\n")

print("File created!")

# READ from a file ("r" mode reads only)
with open("secret_vault.txt", "r") as vault:
    all_secrets = vault.readlines()

print("Full list of vault:")
print(all_secrets)

# EXTRACT using indexing
level_21 = all_secrets[0]
level_22 = all_secrets[1]

print(f"Target 1: {level_21}")
print(f"Target 2: {level_22}")


# --------------------------------------------
# PART 2: LISTS AND LOOPS (No split needed)
# --------------------------------------------
print("\n--- SMALL TEST: LISTS AND LOOPS ---")

# Proper list with quotes around EACH item
passwords = ["kickass", "kickme", "kickyour"]

# ONE loop handles everything
for x in passwords:
    print(x)


# --------------------------------------------
# PART 3: USING .split() TO CREATE A LIST
# --------------------------------------------
print("\n--- USING .split() ---")

# ONE giant string
giant_string = "kickass, kickme, kickyou"

# .split() chops the string into a list at the comma
passwords_split = giant_string.split(", ")

print("After split:")
print(passwords_split)

for x in passwords_split:
    print(x)
