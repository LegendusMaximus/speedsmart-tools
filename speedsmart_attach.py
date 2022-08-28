import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import speedsmart_secrets as settings
import speedsmart_config as config
import shutil

def attach_and_send():
    #assert isinstance(settings.fromemail, list)
    if config.emailsending == 0:
        return
    msg = MIMEMultipart()
    msg['From'] = settings.email
    msg['To'] = COMMASPACE.join(settings.fromemail)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Your full-length SpeedSmart table is ready"
    msg.attach(MIMEText("See attached file."))
    with open(config.fulllength, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(config.fulllength)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(config.fulllength)
        msg.attach(part)
    smtp = smtplib.SMTP(settings.smtp, 587)
    smtp.starttls()
    smtp.login(settings.email, settings.password)
    smtp.sendmail(settings.email, settings.fromemail, msg.as_string())
    smtp.close()
    print("Email sent!")

def send_averages():
    if config.emailsending == 0:
        return
    shutil.make_archive("averages", 'zip', "averages/")
    msg = MIMEMultipart()
    msg['From'] = settings.email
    msg['To'] = COMMASPACE.join(settings.fromemail)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Your averages are ready"
    msg.attach(MIMEText("See attached ZIP file."))
    with open("averages.zip", "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename("averages.zip")
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename("averages.zip")
        msg.attach(part)
    smtp = smtplib.SMTP(settings.smtp, 587)
    smtp.starttls()
    smtp.login(settings.email, settings.password)
    smtp.sendmail(settings.email, settings.fromemail, msg.as_string())
    smtp.close()
    print("Email with averages sent!")
