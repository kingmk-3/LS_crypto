# Decode Bacon's cipher
def bacon_to_text(bacon_text):
    # Bacon's alphabet
    bacon_dict = {
        'AAAAA': 'a', 'AAAAB': 'b', 'AAABA': 'c', 'AAABB': 'd', 'AABAA': 'e',
        'AABAB': 'f', 'AABBA': 'g', 'AABBB': 'h', 'ABAAA': 'i', 'ABAAB': 'k',
        'ABABA': 'l', 'ABABB': 'm', 'ABBAA': 'n', 'ABBAB': 'o', 'ABBBA': 'p',
        'ABBBB': 'q', 'BAAAA': 'r', 'BAAAB': 's', 'BAABA': 't', 'BAABB': 'u',
        'BABAA': 'w', 'BABAB': 'x', 'BABBA': 'y', 'BABBB': 'z'
    }
    
    # Convert to 5-letter chunks
    bacon_chunks = [bacon_text[i:i+5] for i in range(0, len(bacon_text), 5)]
    # Decode each chunk
    decoded_text = ''.join(bacon_dict.get(chunk, '?') for chunk in bacon_chunks)
    
    return decoded_text

# Given Bacon's cipher text
bacon_text = "AAABAABABAAAAAABAAABBAAABABAAAAAABAAAAAAABABAAABAAABBAAAAABABAAAABABBAABBBABAABAABAAAABBABABBAABAAAB"
#Decode
decoded_bacon_text = bacon_to_text(bacon_text)
print(decoded_bacon_text)
