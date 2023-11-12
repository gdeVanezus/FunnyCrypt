# FunnyCrypt
> Encrypting text using Caesar ciphers

> [!NOTE]
> This module was done in 10 minutes

Installing:
```
pip install FunnyCrypt
```

Example:
```py
from FunnyCrypt import FunnyCrypt


shift_value = 3
cryptor = FunnyCrypt(shift_value)

text_to_encrypt = "Hello, World!"
encrypted_text = cryptor.encrypt(text_to_encrypt)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = cryptor.decrypt(encrypted_text)
print(f"Decrypted Text: {decrypted_text}")

```
