# speedsmart-tools
A set of tools to help me export my SpeedSmart table

## About the tools
This set of tools is made specifically for SpeedSmart History files which have been truncated by SpeedSmart (either due to hitting the 3000 speedtests export limit, truncation of network names containing an & character or removal of network names containing a # character). It has been designed to be relatively simple to use, just give it the required files and start it. It outputs a complete file which is useful for data analysis.

## Why is this needed?

This set of tools needs to be created as:
- SpeedSmart for iOS only exports your last 3000 speedtests, and I have more than that. I would like to create a complete table file, and I think others might want to too.
- SpeedSmart will truncate a network name containing the & character, and a program can easily restore those names given a list of what they are supposed to look like (for example, I sometimes speedtest networks called "H&M Free WiFi" and they come through as "H" in SpeedSmart).
- Network names containing a # symbol are not included in the export (i.e. They have a row but the name comes through as "N/A"). It is possible to identify these by IP address and add them back to the file, but this process takes a long time by hand.
- If you do a lot of speedtests, manually pressing "Export" after each one is a pain. This tool can optionally use the SpeedSmart API to auto-export.

## Basic Installation
If you would like to have a go with this on your computer as a one-time experience or manually running it every time, here is how to get it installed:

1. Download the code as a ZIP file or clone the repository.
2. Edit the speedsmart_config.py file with valid file paths.
3. If you are planning to use email functionality, rename speedsmart_secrets_example.py to speedsmart_secrets.py and add details. This is not required for just running main.py or start.py
4. Install the project requirements by using "pip install -r requirements.txt"
5. Run the start.py file to add replacing networks or start the tool. To start the tool without any input first, run main.py

## Email setup instructions
To set up the email system to run continuously, first make sure your secrets file is ready.
If you haven't already, rename speedsmart_secrets_example.py to speedsmart_secrets.py and add your email details (Gmail is recommended). Make sure to use an app password if using Gmail as your actual password cannot be used due to Google's security policy.
DO NOT use your primary email account for this program as it will not work properly. Instead, create a new account and use that.
Once your secrets file is ready, perform the following procedure on a virtual machine or another device that you think will stay turned on:
- Navigate to the correct directory
- Run the command: python3 speedsmart_email.py &
- It will output a process id. Disown this id by typing disown followed by the ID (e.g. disown 12345). This means that the process will not quit when you log out.
- Take note of this ID as you can use kill followed by the ID to stop the program if needed.

## API functionality
Please note: This feature is for very advanced users of this tool only. Users must obtain an API key to use this feature and this is not easy. Beginners/Intermediate users should have a go at the email set up instead.

### Prerequisites
Before you start, you first need a file named speedsmart_secrets.py with the correct settings (a newly-created email address for this program, an app password for that address, the smtp server, and your API key).
The quickest way to make one is to rename speedsmart_secrets_example.py to speedsmart_secrets.py and edit the details to your own options. IMAP server is not needed if you won't be using speedsmart_email.py

Hint: If you just can't figure out how to get hold of an API key, ask yourself these questions:
- What URL does SpeedSmart for iOS request the export from?
- What clue does the "response = ..." line in the speedsmart_api.py file give you?
- How could you find the URL out?

And, maybe after that, you will find your API key...

### Setup
To get this setup running, just use these commands on a virtual machine or other device that will likely stay on for a large amount of time:
- "python3 speedsmart_api.py &"
- Take note of the process ID shown
- "disown [process-id]" Where [process-id] is the ID you took note of.

After that, you are free to log out of the device in question
Please note that only the two strings in quotes are the commands.

## Goals/To Do list
I will check items off below once they are completed and functional

### Core components
- [x] Get back my full length SpeedSmart table
- [x] Restore the full network names for networks containing & or #
- [x] Get the Count column back in my new combined table

### Email features (very useful to enjoy the benefits of this program without having a computer at hand)
- [x] Set up the program to receive exported CSV files from SpeedSmart by email (e.g. to a random Gmail address) and send them back to the sender once processed.
- [ ] Add average calculation as an optional feature to the tool. Maybe calculate these if the user includes a certain string in the email they send to the program (e.g. [[averages=true]])
- [ ] Functionality to add new &/# replacing networks via specially-formatted email
- [x] What is the most secure way to store email server/address/password on a per-user basis?

### Limitations to overcome
- [ ] At the moment, this program will stop being useful after 6000 speedtests. I need a robust plan for continuing to create a full-length table before I hit that limit!
- [ ] If there are two networks that have been truncated to the same thing by SpeedSmart, we need to differentiate them (e.g. by IP address)