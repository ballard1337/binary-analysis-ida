login = "&06'0!"
password = "71='9?"

for i in login:
    print(chr(ord(i) ^ 0x55), end="")

print()

for i in password:
    print(chr(ord(i) ^ 0x55), end="")
