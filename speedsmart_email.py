# Receiving table code taken from https://stackoverflow.com/questions/61366836/download-attachment-from-mail-using-python
import os
from imbox import Imbox
import traceback
import speedsmart_secrets as settings
import speedsmart_tools
import speedsmart_config as config
import speedsmart_attach
import time

while True:
    time.sleep(config.wait)
    host = settings.imap
    username = settings.email
    password = settings.password
    download_folder = "attachments/"

    if not os.path.isdir(download_folder):
        os.makedirs(download_folder, exist_ok=True)
    
    mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
    messages = mail.messages(unread=True, sent_from=settings.fromemail)

    for (uid, message) in messages:
        mail.mark_seen(uid) # optional, mark message as read

        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"{download_folder}/{att_fn}"
                print(download_path)
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
                speedsmart_tools.restore_full_length(config.original, download_path, config.fulllength)
                if config.andnetworks == 0:
                    print("Skipping and replacing")
                else:
                    print("Starting and replacing")
                    speedsmart_tools.and_replacing(config.fulllength)
                if config.hashnetworks == 0:
                    print("Skipping hashtag replacing")
                else:
                    print("Starting hashtag replacing")
                    speedsmart_tools.hashtag_replacing(config.fulllength)
                if config.count == 1:
                    print("Restoring count column")
                    speedsmart_tools.restore_count(config.fulllength)
                print("Finished!")
                speedsmart_attach.attach_and_send()

            except:
                print(traceback.print_exc())

    mail.logout()