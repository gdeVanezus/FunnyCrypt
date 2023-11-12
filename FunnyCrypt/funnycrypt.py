class FunnyCrypt:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        result = ''
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start + self.shift) % 26 + start)
            else:
                result += char
        return result

    def decrypt(self, text):
        result = ''
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start - self.shift) % 26 + start)
            else:
                result += char
        return result


