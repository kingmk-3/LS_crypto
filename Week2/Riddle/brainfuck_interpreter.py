def brainck_interpreter(code):
    tape = [0] * 30000
    ptr = 0
    code_ptr = 0
    loop_stack = []
    output = ""
    
    while code_ptr < len(code):
        command = code[code_ptr]
        
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif command == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif command == '.':
            output += chr(tape[ptr])
        elif command == ',':
            pass  # Input not used in this script
        elif command == '[':
            if tape[ptr] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_ptr += 1
                    if code[code_ptr] == '[':
                        open_brackets += 1
                    elif code[code_ptr] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_ptr)
        elif command == ']':
            if tape[ptr] != 0:
                code_ptr = loop_stack[-1]
            else:
                loop_stack.pop()
        
        code_ptr += 1
    
    return output

# Given Brainfuck code
brainfuck_code = '++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++..----.-.++++++.+++++++++++.-------------------.+++.+++++.>----------.<-----.>----.<-.>---.<-------------------.>--------.-..++.-------.<.>++++++++++++++++.+++++.-------.---------.<+++.>-----.++++++++++++++++..--.<---.>+++.---------------.+++.+.+++++++++++.-----------------.++++++++++++++++.<.>----------.+.--.------.+++++++++++++++++.----------.+++++++++++.-----------.++++++++++.------------.+++++.----------.+.++++++++++++++.-----.---.++.----.+++++++++++++.<++++++++++++++++++.>.<+++++++++.++++.<++++++++++++++++++++.>-----.--..++++.---------.++++.>.<++.+.-.>++++.<-----.>----.<+++++.>---.<.++++.-----.>-.<+.>++++.<.>--.-.<+.--.>+++.<----.>.<+++++++.>---.<<.>>++++.<---.>-.<-.>--.<----.>.-.<++++++.--.>+++++++.<-.---.++++++.>-------.<<.>>++++.<-.++++.-------.--.>.-----.<++++++.<.>--.>++++++++.<-------.>----.<+++++.>-.<<.>++++.--.<+++.>---.-.>++.-.---.<-.+++++++.>+++++++.<-.>-----.++.----.+++++++.----.<-.>++++.<+++.-------.++.>----.<<---.>>--.<++.<+++.>----.>+.<++++++++.>--..+++.<--.>.<---.---.>---.---.<++++.<++++++++.'

# Decode the message
decoded_message = brainck_interpreter(brainfuck_code)
# print(decoded_message)
import base64

decoded_bytes = base64.b32decode(decoded_message)
decoded_bytes = base64.b32decode(decoded_bytes)
decoded_bytes = base64.b32decode(decoded_bytes)
decoded_bytes = base64.b32decode(decoded_bytes)
decoded_bytes = base64.b32decode(decoded_bytes)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)
#after this we need to appply the vigenere cipher
def vigenere_decrypt(ciphertext, key):
    # Convert the key to uppercase
    key = key.upper()
    plaintext = ''
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():  
            char = char.upper()
            #the position of the character in the alphabet (0-25)
            char_pos = ord(char) - ord('A')

            #the position of the corresponding key character in the alphabet (0-25)
            key_pos = ord(key[i % key_length]) - ord('A')
            
            # Decrypted the character
            decrypted_char = chr((char_pos - key_pos + 26) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            # If the character is not alphabetic, add it to the plaintext without decrypting
            plaintext += char
    
    return plaintext

plaintext = vigenere_decrypt(decoded_string, "KEY")
print(f"Decrypted text: {plaintext.lower()}")
