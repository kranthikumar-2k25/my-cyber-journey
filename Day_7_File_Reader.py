file = open("secret.txt", "w")
file.write("target ip is 192.180.1.90")
file.close()

file = open("secret.txt", "r")
content = file.read()

print("hacker alert", content)

file.close()
