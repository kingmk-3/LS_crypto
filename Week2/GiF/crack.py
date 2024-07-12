from sympy.ntheory.factor_ import totient
from sympy import mod_inverse
#Just the list of parameter obtained from rot47
n=[23270927,119750403]
e=[65537,257]
phi=[totient(n[0]),totient(n[1])]
c=[3872687,58519946]
d=[None]*2
#this gets back the original message
for i in range(2):
    d[i]=mod_inverse(e[i],phi[i])
cipher_decrypted = [pow(c[i], d[i],n[i]) for i in range(2)]
print(cipher_decrypted)

#Takes each of the elements in cipher_decrypted and put them one by one
byte_array=[None]*len(cipher_decrypted)
original_message=[None]*len(cipher_decrypted)
for i in range(len(cipher_decrypted)):
    # Determine the number of bytes required to represent the integer
    # This can be done using (cipher_decrypted[0].bit_length() + 7) // 8
    num_bytes = (cipher_decrypted[i].bit_length() + 7) // 8

    # Convert the integer back to a byte array
    byte_array[i] = cipher_decrypted[i].to_bytes(num_bytes, byteorder='big')

    # Convert the byte array back to a string using the same encoding (UTF-8)
    original_message[i] = byte_array[i].decode('utf-8')

print("Byte Array:", byte_array)
print("Original Message:", original_message)
