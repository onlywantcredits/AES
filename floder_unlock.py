import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cryptography.fernet import Fernet

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            # 取得檔案名
            encrypted_file_name = os.path.basename(event.src_path)

             #讀取儲存的私鑰
            with open('key\\key.pem', 'rb') as f:
             key_data = f.read()
            
            # 讀取要解密的檔案
            with open("save_folder\\"+encrypted_file_name, "rb") as f:
             fernet = Fernet(key_data)
             encrypted = f.read()
             # 使用對稱性私鑰解密檔案
             decrypted = fernet.decrypt(encrypted)

            #將解密後的檔案存儲到資料夾上
            with open("unlock_floder\\unlock"+encrypted_file_name, "wb") as f:
             f.write(decrypted)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='unlock', recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
