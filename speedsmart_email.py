# Receiving table code taken from https://stackoverflow.com/questions/61366836/download-attachment-from-mail-using-python
import os
from imbox import Imbox
import traceback
import speedsmart_secrets as settings
import speedsmart_tools
import speedsmart_config as config
import speedsmart_attach
import time
import speedsmart_email_function
import logging

logging.basicConfig(filename="speedsmart_email.log",level=logging.ERROR)

try:
    while True:
        time.sleep(config.wait)
        if config.emailoutput == 1:
            print("Checking email address...")
        speedsmart_email_function.check()
except Exception as err:
    logging.error(err)
    print(err)