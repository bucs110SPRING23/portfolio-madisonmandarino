def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = 8  + 6
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        result += char
    return result


message = caesar_cipher("The quick brown fox jumps over the lazy dog", 19 )


encrypted_message = open("encrypted.txt", "w")
encrypted.write(message)
encrypted.close()