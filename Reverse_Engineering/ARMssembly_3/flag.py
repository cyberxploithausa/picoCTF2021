
#!/usr/bin/env python3

target = 4012702611

result = 0
while target != 0:
    if target & 1 != 0:
        result += 3
    target >>= 1

print(hex(result))
