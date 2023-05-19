def decrypt(ciphered, key):
    deciphered = ""
    for i in range (len(ciphered)):
        ascii_no = ord(ciphered[i])
        if 127 > ascii_no > 31:
            ascii_no = ((ascii_no - ord(key[i]) - 32 ) % 95 ) + 32 
        deciphered += chr(ascii_no)
    return deciphered    