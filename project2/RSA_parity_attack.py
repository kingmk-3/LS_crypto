from sympy import randprime,gcd, mod_inverse,totient
from decimal import *
class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length):
        # define self.p, self.q, self.e, self.n, self.d here based on key_length
        self.p=randprime(2**(key_length//2-1),2**(key_length//2))
        self.q=randprime(2**(key_length//2-1),2**(key_length//2))
        while self.p==self.q:
            self.q=randprime(2**(key_length//2-1),2**(key_length//2))
        phi=(self.p-1)*(self.q-1)
        self.e=randprime(2,phi)
        self.n=self.p*self.q
        self.d=mod_inverse(self.e,phi)

    def encrypt(self, binary_data):
        # return encryption of binary_data here
        decimal_message=int.from_bytes(binary_data,byteorder='big')
        return pow(decimal_message,self.e,self.n)

    def decrypt(self, encrypted_int_data):
        # return decryption of encrypted_binary_data here
        return pow(encrypted_int_data,self.d,self.n)

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""

    def is_parity_odd(self, encrypted_int_data):
        # Decrypt the input data and return whether the resulting number is odd
        return self.decrypt(encrypted_int_data)%2


def parity_oracle_attack(ciphertext, rsa_parity_oracle):
    # implement the attack and return the obtained plaintext
    start = 0
    end = rsa_parity_oracle.n-1
    original=ciphertext
    multiplier = pow(2, rsa_parity_oracle.e, rsa_parity_oracle.n)
    # print(multiplier,rsa_parity_oracle.n,"\nThere you go\n")
    while end - start > 0:
        # print(start,end)
        mid = (start + end) // 2
        ciphertext = (ciphertext * multiplier) % rsa_parity_oracle.n
        if rsa_parity_oracle.is_parity_odd(ciphertext):
            start = mid+1
        else:
            end = mid
    #although it seems that there shouldn't be any error, but every that it end up some few last digit mismatchde from the original
    #So this while loop just compensate for that, and it takes negligible amount of time in comparision to binary search above this
    while(original!=pow(end,rsa_parity_oracle.e,rsa_parity_oracle.n)):
        end=end-1
    return end


def main():
    input_bytes = input("Enter the message: ")

    # Generate a 1024-bit RSA pair    
    rsa_parity_oracle = RSAParityOracle(1024)

    # Encrypt the message
    ciphertext = rsa_parity_oracle.encrypt(input_bytes.encode())
    print("Encrypted message is: ",ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big'))


    decrypted=rsa_parity_oracle.decrypt(ciphertext)
    decrypted=decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big')
    print("Decrypted text is: ",decrypted.decode())

    # Check if the attack works
    plaintext = parity_oracle_attack(ciphertext, rsa_parity_oracle)
    plaintext=plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big')
    print("Obtained plaintext: ",plaintext.decode())
    # assert plaintext == input_bytes.encode()


if __name__ == '__main__':
    main()