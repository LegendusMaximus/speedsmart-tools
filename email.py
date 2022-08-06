# Receiving table code taken from https://stackoverflow.com/questions/61366836/download-attachment-from-mail-using-python
import os
from imbox import Imbox # pip install imbox
import traceback
import speedsmart_secrets as settings

# enable less secure apps on your google account
# https://myaccount.google.com/lesssecureapps

host = settings.imap
username = settings.email
password = settings.password
download_folder = "attachments/"

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(unread=true, sent_from=settings.fromemail)

for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}/{att_fn}"
            print(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
        except:
            print(traceback.print_exc())

mail.logout()