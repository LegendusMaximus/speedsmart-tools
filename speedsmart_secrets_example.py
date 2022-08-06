# SpeedSmart Secrets - Example
# This is an example of what a secrets file should look like. To use this file, change the name to something else (e.g. speedsmart_secrets.py) and make sure that this is reflected in the import statement at the top of the email.py file.

# The email address you would like this program to use. This should not be used by other devices/apps.
email = "example@example.com"

# The password for the account
# For Gmail, an app password is required and 2-Step verification must be enabled to create these
password = "password"

# The SMTP server to use.
# For Gmail, use smtp.gmail.com:587
# For Outlook, use smtp-mail.outlook.com:587
# If you have a different email provider, look up the SMTP domain and port for Starttls
smtp = "smtp.example.com:587"

# The imap server for receiving the emails
imap = "imap.example.com"

# The email address you will be sending your tables from
fromemail = "example123@email.com"