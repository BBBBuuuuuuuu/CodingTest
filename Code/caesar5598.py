str = input()

changed_str = ''
for char in str:
    changed_char = ord(char)
    if 65 <= changed_char <= 67:
        changed_str += chr(changed_char + 23)
    else:
        changed_str += chr(changed_char - 3)


print(changed_str, end='')