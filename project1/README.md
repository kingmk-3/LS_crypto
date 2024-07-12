# Project 1: Hill Cipher

## Clarification Regarding Convention

Currently, if the key is `GYBNQKURP`, then it's represented as:
\[ K = \begin{pmatrix} 6 & 24 & 1 \\ 13 & 16 & 10 \\ 20 & 17 & 15 \end{pmatrix} \]

while a message `nameis` is represented as:
\[ P = \begin{pmatrix} 13 & 4 \\ 0 & 8 \\ 12 & 18 \end{pmatrix} \]

## Description of the Function in `project.py`

### Commenting and Modes

The script is well-commented to ensure clarity. It includes four modes:

1. **Encryption**: Encrypts the given plaintext using the provided key.
2. **Key Discovery**: Discovers one possible key from the solution space.
3. **All Key Discovery**: Discovers all possible keys from the solution space.
4. **Exit**: Exits the script.

Additionally, the script prompts the user each time to decide whether to change the key.

### Difference Between Mode 2 and Mode 3

- **Mode 2**: Returns only one key from the solution space.
- **Mode 3**: Returns all possible keys from the solution space.

## Concept for Key Discovery

The basic concept of linear algebra is used for key discovery. We start with the equation:

\[
K \cdot P = C
\]

which implies:

\[
P^{T} \cdot K^{T} = C^{T}
\]

We find the solution space for each column of \( K^{T} \). Then, we take those combinations of columns that result in an invertible matrix \( K \).

### Steps for Key Discovery

1. **Transpose the Equations**:
   - From \( K \cdot P = C \), we transpose to \( P^{T} \cdot K^{T} = C^{T} \).
2. **Find Solution Space**:
   - Determine the solution space for each column of \( K^{T} \).
3. **Check Invertibility**:
   - Combine columns that result in an invertible matrix \( K \).

### Example

If you have a plaintext matrix \( P \) and a ciphertext matrix \( C \), you solve for \( K \) as follows:

\[
P^{T} \cdot K^{T} = C^{T}
\]

Given \( P \) and \( C \), you can find \( K \) by solving the system of linear equations and ensuring that the resulting matrix is invertible.

This method ensures that we can discover valid keys that can be used for decryption.

## Usage

Run the script and follow the prompts to select the desired mode and provide the necessary input for encryption or key discovery.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact Information

For any questions or concerns, please contact:

- Your Name: [your.email@example.com](mailto:your.email@example.com)
