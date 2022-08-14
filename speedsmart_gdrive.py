# This module uploads a given file to Google drive. If you haven't used it before, you will need to authorise it with your Google account first by running it.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import speedsmart_secrets as settings
import speedsmart_config as config

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("gdrive_credentials.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
# Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("gdrive_credentials.txt")

def upload(filepath):
    drive = GoogleDrive(gauth)
    gfile = drive.CreateFile({"parents":[{"id": settings.driveid}]})
    gfile.SetContentFile(filepath)
    gfile.Upload()
    print("File \""+filepath+"\" uploaded")
