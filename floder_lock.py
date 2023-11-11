import os
import time
from cryptography.fernet import Fernet

folder_path = 'data_floder'

while True:
    # 列出資料夾中的所有檔案
    files = os.listdir(folder_path)
    
    # 如果有新檔案進來就顯示它們的名字，然後刪除它們
    if len(files) > 0:
        print("檔案:")
        for file in files:
             # 取得檔案名
            encrypted_file_name =  os.path.basename(file)

            #讀取儲存的鑰匙
            with open('key\\key.pem', 'rb') as f:
             key_aes = f.read()
             fernet = Fernet(key_aes)

            # 加密文件並保存在資料夾
            with open("data_floder\\"+encrypted_file_name, 'rb') as file:
                original = file.read()
                encrypted = fernet.encrypt(original)
                with open(os.path.join('save_folder', encrypted_file_name), 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
 
            os.remove(os.path.join(folder_path, encrypted_file_name))
    
    # 等待一段時間後再檢查是否有新檔案
    time.sleep(10)
