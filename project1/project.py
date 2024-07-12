import numpy as np
import re
from sympy import Matrix
print("Mode = 1 : For converting given plaintext to cipher, 2: Discover key from plain text and cipher(returns only one possible key), 3: To get a list of all possible keys for given plaintext and cipher, 4: To exit ")
key=np.array([[6,24,1],[13,16,10],[20,17,15]])#this is the defualt key

def convert_text_to_matrix(text,n):
    text=text.upper()
    text = re.sub(r'[^a-zA-Z]', '', text)#this is to make sure that no other character than alphabets passes
    if len(text) % n != 0:#this is to adjust the length so that its multiple of n
        remainder = len(text) % n
        num_x_needed = n - remainder
        text += "X" * num_x_needed
    matrix=np.array([ord(x)-65 for x in text]).reshape(-1,n).T
    return matrix

def convert_matrix_to_text(matrix):
    text=""
    text+="".join([chr(x+65) for x in matrix.T.reshape(-1)])
    return text

def convert_plainttext_to_cipher(text,key):
    matrix=convert_text_to_matrix(text,key.shape[0])
    assert(DET(key,26)!=0)
    return convert_matrix_to_text(np.matmul(key,matrix)%26)

def solve_column(A, b, mod):
    #This gives the solution space for a coloumn of key.T
    solutions = []
    for i in range(mod):
        for j in range(mod):
            for k in range(mod):
                x = np.array([i, j, k])
                if np.array_equal((np.matmul(A, x) % mod), b):
                    solutions.append(x)
    return solutions

def brute_force_discover_key(plaintext, ciphertext):
    #This is a uses the solution space of each coloumn of key.T, then naively checks which combination of them statisfies
    plaintext_matrix = convert_text_to_matrix(plaintext, 3).T
    ciphertext_matrix = convert_text_to_matrix(ciphertext, 3).T
    
    # Gets solution spaces for each column of the key matrix
    solution_spaces = []
    for i in range(3):
        solutions = solve_column(plaintext_matrix, ciphertext_matrix[:, i], 26)
        solution_spaces.append(solutions)
    
    # Check all combinations of solutions to form candidate key matrices
    for col1 in solution_spaces[0]:
        for col2 in solution_spaces[1]:
            for col3 in solution_spaces[2]:
                candidate_key = np.array([col1, col2, col3])
                if DET(candidate_key,26)!=0:
                    if np.array_equal(np.matmul(candidate_key, plaintext_matrix.T) % 26, ciphertext_matrix.T):
                        return candidate_key
    return None

def brute_force_discover_all(plaintext,ciphertext):
    #This is a uses the solution space of each coloumn of key.T, then naively checks which combination of them statisfies
    plaintext_matrix = convert_text_to_matrix(plaintext, 3).T
    ciphertext_matrix = convert_text_to_matrix(ciphertext, 3).T
    
    # Gets solution spaces for each column of the key matrix
    solution_spaces = []
    for i in range(3):
        solutions = solve_column(plaintext_matrix, ciphertext_matrix[:, i], 26)
        solution_spaces.append(solutions)
    
    # Check all combinations of solutions to form candidate key matrices
    all_keys=[]
    for col1 in solution_spaces[0]:
        for col2 in solution_spaces[1]:
            for col3 in solution_spaces[2]:
                candidate_key = np.array([col1, col2, col3])
                if DET(candidate_key,26)!=0:
                    if np.array_equal(np.matmul(candidate_key, plaintext_matrix.T) % 26, ciphertext_matrix.T):
                        all_keys.append(convert_matrix_to_text(candidate_key.T))
    return all_keys

def DET(matrix, mod):
    det = int(np.round(np.linalg.det(matrix))) % mod
    return det


#user interface

separtor="%%"*50
print(separtor)
while True:
    change = input("Enter 1 (if you want to change the default/previous key) or 0 (otherwise): ")
    if change == '1':
        x = input("Entry your key (as a single string eg: "+"GYBNQKURP"+" given as key [[6 24 1],[13 16 10],[20 17 15]] ): ")
        n = int(input("Enter the value of n: "))
        key_values = [ord(char) - 65 for char in x.replace(" ", "")]
        assert len(key_values) == n * n, "The length of the key values must be equal to n*n."
        key = np.array(key_values).reshape(n, n)
        print("New key matrix set:")
        print(key)
    
    mode = input("Enter your mode (1: plaintext to cipher,2: One key from plaintext and cipher, 3: All keys from plaintext and cipher, 4: to exit): ")
    if mode == '1':
        text = input("Enter your input string: ")
        cipher_text = convert_plainttext_to_cipher(text, key)
        print("Cipher Text:", cipher_text)
    elif mode == '4':
        break
    elif mode == '2':
        plaintext = input("Enter the known plaintext: ")
        ciphertext = input("Enter the corresponding ciphertext: ")
        print("We assume the key to 3*3")
        discovered_key = brute_force_discover_key(plaintext,ciphertext)
        print("Discovered Key Matrix:")
        print(convert_matrix_to_text(discovered_key.T))
    elif mode=='3':
        plaintext = input("Enter the known plaintext: ")
        ciphertext = input("Enter the corresponding ciphertext: ")
        print("We assume the key to 3*3")
        discovered_key = brute_force_discover_all(plaintext,ciphertext)
        print("Discovered Key Matrix:")
        print(discovered_key)
    else:
        print("Invalid mode selected. Please enter 1 or 2.")
    print(separtor)

# def mod_inv_matrix(matrix): 
#     det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
#     det_inv = pow(det, -1,26)  # Modular inverse of the determinant
#     matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % 26
#     return matrix_mod_inv

# def convert_cipher_to_plaintext(text, key):
#     matrix = convert_text_to_matrix(text, key.shape[0])
#     assert (DET(key,26)!=0)
#     key_inv_mod = mod_inv_matrix(key)
#     return convert_matrix_to_text(np.matmul(key_inv_mod, matrix) % 26)