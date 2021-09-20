#!/usr/bin/env python3
import hashlib

username_trial = b"MORTON"
digest = hashlib.sha256(username_trial).hexdigest()

print(f"index 4: {digest[4]}")
print(f"index 5: {digest[5]}")
print(f"index 3: {digest[3]}")
print(f"index 6: {digest[6]}")
print(f"index 2: {digest[2]}")
print(f"index 7: {digest[7]}")
print(f"index 1: {digest[1]}")
print(f"index 8: {digest[8]}")

flag_part_1 = "picoCTF{1n_7h3_|<3y_of_"
flag_part_2 = ""
flag_part_2 += digest[4] + digest[5]
flag_part_2 += digest[3] + digest[6]
flag_part_2 += digest[2] + digest[7]
flag_part_2 += digest[1] + digest[8]
flag_part_3 = "}"

print(f"flag: {flag_part_1 + flag_part_2 + flag_part_3}")
