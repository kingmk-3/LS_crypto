
def apply_rot47(s):
    result = []
    for char in s:
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:
            result.append(chr(33 + ((ascii_val - 33 + 47) % 94)))
        else:
            result.append(char)
    return ''.join(result)

#output of the Frame_merger
strings = ["?`labaf_haf", "6`leddbf", "4`lbgfaegf", "?al``hfd_c_b", "6aladf", "4aldgd``hhce"]

# Apply ROT47 to each string
rot47_strings = [apply_rot47(s) for s in strings]
print(rot47_strings)
