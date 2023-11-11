import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            # 取得檔案名
            filename =  os.path.basename(event.src_path)
            # 設定寄件人、收件人、主旨、內容等資訊
            from_email = 'ewdscxqaz0936@gmail.com'
            to_email = '109316117@gms.tcu.edu.tw'
            subject = '檔案附件'
            body = '這是一封測試郵件，請勿回覆。'

            # 建立郵件物件
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            # 添加郵件內容
            msg.attach(MIMEText(body, 'plain'))

            # 讀取檔案
            with open(event.src_path, 'rb') as f:
                # 建立MIMEApplication，將檔案加入到郵件中
                attachment = MIMEApplication(f.read(), _subtype='txt')
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(attachment)

            # 使用SMTP協議發送郵件
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'ewdscxqaz0936@gmail.com'
            smtp_password = 'njnmdeagxvzroamw'

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(from_email, to_email, msg.as_string())
            
            

if __name__ == "__main__":
 
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='email_floder', recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()