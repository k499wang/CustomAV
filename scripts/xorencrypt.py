import argparse

def xor(value,key):
    encrypted = []
    for i, char in enumerate(value):
        # ord(char) returns the ASCII value of the character
        encrypted_char = ord(char) ^ ord(key[i % len(key)])
        encrypted.append(f"{encrypted_char:02x}")  # Convert to hex base 16 number, 02 means that it should always be 2 characters long
        
    
    return ''.join(encrypted)


def decrypt(value, key):
    decrypted = []
    for i in range(0, len(value), 2):
        encrypted_chars = value[i:i+2]
        int_char = int(encrypted_chars, 16)  # Convert the hex number to an integer, back to base 10 (like the ascii in the xor function)
        decrypted_char = chr(int_char ^ ord(key[(i // 2) % len(key)]))
        decrypted.append(decrypted_char)
    
    return ''.join(decrypted)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Encrypt a string using XOR encryption")
    argparser.add_argument("value", help="The value to encrypt")
    argparser.add_argument("key", help="The key to encrypt the value with")
    
    args = argparser.parse_args()
    
    print(xor(args.value, args.key))
    print(decrypt(xor(args.value, args.key), args.key))
    
    
    
    
    
        # based on the index of the character in the key, we XOR the ASCII value of the character with the ASCII value of the character in the key
        # we use the modulo operator to loop through the key if the length of the key is less than the length of the value
        # instead of just taking one letter from the key and using it to xor the whole value, we loop through the key, this makes it harder to crack
        
# After converting it into ASCII, we convert it into binary, and then we xor it.
# Remember that you can use the same algorithm to xor the encrypted text with the key to get the original text back.
# A xor A = 0, A xor 0 = A, so we get the same thing back after xoring it two times!
# (a xor b) xor b = a is the basis of our algorithm
# = a xor (b xor b) = a xor 0 = a