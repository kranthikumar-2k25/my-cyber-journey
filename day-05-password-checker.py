print("--- SYSTEM PASSWORD CREATOR ---")

password = input("enter the password(must be atleast 8 characters):")

if len(password) < 8:
  print("too short")

else:
  print("password accepted")
