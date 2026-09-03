# ============================================
# DAY 19: PYTHON .split() AND \n (NEWLINE)
# ============================================

print("--- PYTHON VS LINUX CUT COMMAND ---")

# This simulates the raw output from Linux md5sum command
# It has the barcode, extra spaces, and a dash at the end
raw_shredder_output = "8ca319486bfbbc3663ea0c813483639d  -"

print("Raw Output:")
print(raw_shredder_output)

# .split() chops the string into a list at every space
# [0] grabs the FIRST item from that list (the barcode)
barcode = raw_shredder_output.split()[0]

# \n means "press Enter" (adds a blank line). It does NOT delete anything!
print("\nClean Barcode:")
print(barcode)

print("\n--- SHOWING THE LIST AFTER SPLIT ---")

# Let's see the full list that .split() creates
full_list = raw_shredder_output.split()
print(full_list)

print("\nIndex [0] =", full_list[0])  # The barcode
print("Index [1] =", full_list[1])  # The dash

print("\n--- PROVING \n JUST ADDS SPACE ---")

print("Line 1")
print("Line 2")
print("\nLine 3")
print("See the blank line above? That is \\n pressing Enter. Nothing was deleted.")
