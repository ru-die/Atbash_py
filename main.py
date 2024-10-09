import re
message=input()
new_message = ""
for i in str(message):
    if re.search(r'[A-Z]',i):
        new_message+=chr(26-(ord(i)-64)+1+64)
    elif re.search(r'[a-z]',i):
        new_message+=chr(26-(ord(i)-96)+1+96)
    else:
        new_message+=i
print(new_message)