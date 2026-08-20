print("--- SYSTEM PASSWORD CREATOR ---")

while True:
  password = input("enter the password(atleast 8 characters):")
  if len(password) < 8:
    print("too short.")
  else:
    print("password accepted.")
    break
