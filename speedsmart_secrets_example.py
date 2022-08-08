# SpeedSmart Secrets - Example
# This is an example of what a secrets file should look like. To use this file, change the name to something else (e.g. speedsmart_secrets.py) and make sure that this is reflected in the import statement at the top of the email.py file.

# The email address you would like this program to use. This should not be used by other devices/apps.
email = "example@example.com"

# The password for the account
# For Gmail, an app password is required and 2-Step verification must be enabled to create these
password = "password"

# The SMTP server to use.
# For Gmail, use smtp.gmail.com
smtp = "smtp.example.com"

# The imap server for receiving the emails
# For Gmail, use imap.gmail.com
imap = "imap.example.com"

# The email address you will be sending your tables from
fromemail = "example123@email.com"

# API KEY - Only required if using speedsmart_api
apikey = "XXXXXXXXXXX"