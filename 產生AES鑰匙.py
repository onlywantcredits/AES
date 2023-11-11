from cryptography.fernet import Fernet

# 產生 AES 金鑰

key_aes = Fernet.generate_key()
           
# 取得鑰匙
#fernet = Fernet(key_aes)

# 儲存金鑰
with open('key\\key.pem', 'wb') as f:
    f.write(key_aes)
