# speedsmart-tools
A set of tools to help me export my SpeedSmart table

## About the tools
This set of tools is made specifically for SpeedSmart History files which have been truncated by SpeedSmart (either due to hitting the 3000 speedtests export limit, truncation of network names containing an & character or removal of network names containing a # character). It has been designed to be relatively simple to use, just give it the required files and start it. It outputs a complete file which is useful for data analysis.

### What does the program do?
Once the program receives an exported SpeedSmart table either manually, via email or via the API, it will perform the following tasks in order:

1. If the table has hit the length limit (e.g. has been truncated at the top due to being longer than 3000 rows), the program will insert as many rows as needed from the original.csv (or equivalent) file to create a full-length table.
2. If the "& replacing" feature is enabled, the program will check if any of the network names in the table match the truncated network name the user has entered. If they do, the program will replace them with the full, correct name of the network the user has entered.
3. If the "# replacing" feature is enabled, the program will check if any of the IP addresses in the table are present in the list of IP addresses and network names. If there are any matches, the network name that matches the IP address in question will be added. This feature is needed as any network name starting with a hashtag (#) is not saved by older versions of SpeedSmart.
4. The program will re-do the count column in the table and optionally email it back to the user.

### Supported app versions

This tool is mainly aimed at SpeedSmart for iOS version 7.6.15, which is quite ancient now! The reason it is made for this version is due to this one being the most accessible and me managing to stay on it. Features may or may not work with newer/older versions of SpeedSmart.
The core logic of the program will likely still work as expected but SpeedSmart may haveupdated their API in newer versions so the API request part may not work.

### Why is this needed?

This set of tools needs to be created as:
- SpeedSmart for iOS only exports your last 3000 speedtests, and I have more than that. I would like to create a complete table file, and I think others might want to too.
- SpeedSmart will truncate a network name containing the & character, and a program can easily restore those names given a list of what they are supposed to look like (for example, I sometimes speedtest networks called "H&M Free WiFi" and they come through as "H" in SpeedSmart).
- Network names containing a # symbol are not included in the export (i.e. They have a row but the name comes through as "N/A"). It is possible to identify these by IP address and add them back to the file, but this process takes a long time by hand.
- If you do a lot of speedtests, manually pressing "Export" after each one is a pain. This tool can optionally use the SpeedSmart API to auto-export.

## Basic Installation
If you would like to have a go with this on your computer as a one-time experience or manually running it every time, here is how to get it installed:

1. Download the code as a ZIP file or clone the repository.
2. Edit the speedsmart_config.py file with valid file paths and change settings if desired. There are comments in the file above each setting to tell you what it does.
3. Install the project requirements by using "pip install -r requirements.txt"
4. Run the start.py file to add replacing networks or start the tool. To start the tool without any input first, run main.py

If you are interested in running the tool continuously using emails or the SpeedSmart API as a trigger, have a look at the following sections.

## Optional features
You can read about the optional features this program comes with below.

### Email System
The speedsmart_email.py file allows this program to automatically receive exported SpeedSmart tables via email and run the necessary actions on them before emailing the user back a full-length, correct table. It is possible to set up this file to run continuously so that you do not need to open a computer every time you export your SpeedSmart table.

#### Prerequisites
To set up the email system to run continuously, first make sure your secrets file is ready.
If you haven't already, rename speedsmart_secrets_example.py to speedsmart_secrets.py and add your email details (Gmail is recommended). Make sure to use an app password if using Gmail as your actual password cannot be used due to Google's security policy.
DO NOT use your primary email account for this program as it will not work properly. Instead, create a new account and use that.

#### Setup instructions
Once your secrets file is ready, perform the following procedure on a virtual machine or another device that you think will stay turned on:
- Navigate to the correct directory
- Run the command: python3 speedsmart_email.py &
- It will output a process id. Disown this id by typing disown followed by the ID (e.g. disown 12345). This means that the process will not quit when you log out.
- Take note of this ID as you can use kill followed by the ID to stop the program if needed.

The email system has only been tested with Gmail IMAP and SMTP servers, but may work with other providers that support starttls for SMTP and SSL for IMAP.

### API functionality
This program can be set up to automatically check the SpeedSmart API every 3 minutes for new speedtests from a specific device. If it finds any, it will run through all the different parts of this tool and send the file to the user via email.

Please note: This feature is for very advanced users of this tool only. Users must obtain an API key to use this feature and this is not easy. Beginners/Intermediate users should have a go at the email set up instead. The feature is also unlikely to work if you are on a newer version of SpeedSmart than 7.6.15, but you are welcome to have a go at creating a new file (e.g. speedsmart_new_versions_api.py) and changing the way the URL for the request is put together in that file.

#### Prerequisites
Before you start, you first need a file named speedsmart_secrets.py with the correct settings (a newly-created email address for this program, an app password for that address, the smtp server, and your API key).
The quickest way to make one is to rename speedsmart_secrets_example.py to speedsmart_secrets.py and edit the details to your own options. IMAP server is not needed if you won't be using speedsmart_email.py

Hint: If you just can't figure out how to get hold of an API key, ask yourself these questions:
- What URL does SpeedSmart for iOS request the export from?
- What clue does the "response = ..." line in the speedsmart_api.py file give you?
- How could you find the URL out?

And, maybe after that, you will find your API key...

#### Setup
To get this setup running, just use these commands on a virtual machine or other device that will likely stay on for a large amount of time:
- "python3 speedsmart_api.py &"
- Take note of the process ID shown
- "disown [process-id]" Where [process-id] is the ID you took note of.

After that, you are free to log out of the device in question
Please note that only the two strings in quotes are the commands.

## Goals/To Do list

I will check items off below once they are completed and functional. 

### Core components
- [x] Get back my full length SpeedSmart table
- [x] Restore the full network names for networks containing & or #
- [x] Get the Count column back in my new combined table

### Useful, but not essential, features
- [x] Automate table exports by using the SpeedSmart API
- [ ] Add average calculation as an optional feature to the tool. Maybe calculate these if the user includes a certain string in the email they send to the program (e.g. [[averages=true]])
- [ ] Create a simple Django webpage with ISP averages and other information obtained from the SpeedSmart table

### Email features (very useful to enjoy the benefits of this program without having a computer at hand)
- [x] Set up the program to receive exported CSV files from SpeedSmart by email (e.g. to a random Gmail address) and send them back to the sender once processed.
- [ ] Functionality to add new &/# replacing networks via specially-formatted email
- [x] What is the most secure way to store email server/address/password on a per-user basis?

### Limitations to overcome
- [x] At the moment, this program will stop being useful after 6000 speedtests. I need a robust plan for continuing to create a full-length table before I hit that limit! (Solution: Make the original.csv file longer than 3000 by using a generated full-length file instead of it if needed.)
- [ ] If there are two networks that have been truncated to the same thing by SpeedSmart, we need to differentiate them (e.g. by IP address)