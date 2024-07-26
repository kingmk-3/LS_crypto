# Clarification Regarding the Methods Used

## Binary Search

The parity attack was implemented using a binary search approach for the encrypted message. Here is how it works:

Let's say the message \( m \) (after converting strings to integers), and \( c \) is the corresponding ciphered value. Now, we know that \( m < n \). If we multiply \( c \) with \( 2^{e} \) to obtain \( c' \) and take modulo \( n \), we get \( 2m \mod n \) from the decryption of \( c' \). Now, if the parity oracle says it's even, that means \( 2m \leq n \); otherwise, \( 2m > n \). Hence, a binary search can be implemented using this fact.

## Error Correction

Due to precision errors, after performing the binary search, we might have a few end digits mismatched. To correct this, we perform a linear search around the obtained end value. The search space has already been significantly reduced by the binary search, so it's acceptable to do a linear search to correct for the error. This takes negligible time compared to the binary search.

## String to Integer Conversion

For converting a string to an integer, I used base 256. Specifically, I utilized the `int.from_bytes` method to achieve this.
