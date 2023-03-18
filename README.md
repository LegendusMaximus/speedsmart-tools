# speedsmart-tools
A set of tools to help me export my SpeedSmart table

## About the tools
This set of tools is made specifically for SpeedSmart History files which have been truncated by SpeedSmart (either due to hitting the 3000 speedtests export limit, truncation of network names containing an & character or removal of network names containing a # character). It has been designed to be relatively simple to use, just give it the required files and start it. It outputs a complete file which is useful for data analysis.

These tools have helped me create an entire [dataset of WiFi speeds](https://wifiallaroundthe.eu)

### What is SpeedSmart?

SpeedSmart is a website and cross-platform app used for testing your internet speed. It is simular to other speedtest sites such as speedtest.net, but is more accessible and generates a great exportable table full of stats.

### What does the program do?
Once the program receives an exported SpeedSmart table either manually, via email or via the API, it will perform the following tasks in order:

1. If the table has hit the length limit (i.e. has been truncated at the top due to being longer than 3000 rows), the program will insert as many rows as needed from the original.csv (or equivalent) file to create a full-length table.
2. If the "& replacing" feature is enabled, the program will check if any of the network names in the table match the truncated network name the user has entered. If they do, the program will replace them with the full, correct name of the network the user has entered.
3. If the "# replacing" feature is enabled, the program will check if any of the IP addresses in the table are present in the list of IP addresses and network names. If there are any matches, the network name that matches the IP address in question will be added. This feature is needed as any network name starting with a hashtag (#) is not saved by older versions of SpeedSmart.
4. The program will re-do the count column in the table and optionally email it back to the user.

### Supported app versions

This tool is mainly aimed at SpeedSmart for iOS version 7.6.15, which is quite ancient now! The reason it is made for this version is due to this one being the most accessible and me managing to stay on it. Features may or may not work with newer/older versions of SpeedSmart.
The core logic of the program will likely still work as expected but SpeedSmart may haveupdated their API in newer versions so the API request part may not work.

### Why is this program needed?

This set of tools needs to be created as:
- SpeedSmart for iOS only exports your last 3000 speedtests, and I have more than that. I would like to create a complete table file, and I think others might want to too.
- SpeedSmart will truncate a network name containing the & character, and a program can easily restore those names given a list of what they are supposed to look like (for example, I sometimes speedtest networks called "H&M Free WiFi" and they come through as "H" in SpeedSmart).
- Network names containing a # symbol are not included in the export (i.e. They have a row but the name comes through as "N/A"). It is possible to identify these by IP address and add them back to the file, but this process takes a long time by hand.
- If you do a lot of speedtests, manually pressing "Export" after each one is a pain. This tool can optionally use the SpeedSmart API to auto-export.

## Basic Installation Steps

If you would like to have a go with this on your computer as a one-time experience or manually running it every time, here is how to get it installed:

1. Download the code as a ZIP file or clone the repository and then navigate to the root directory of the repository.
2. Install the project requirements by using "pip install -r requirements.txt"
3. Edit the speedsmart_config.py file with valid file paths and change settings if desired. There are comments in the file above each setting to tell you what it does.
4. Rename speedsmart_secrets_example.py to speedsmart_secrets.py. For basic usage, you can leave all the options in this file as they are.
5. Run the start.py file to start the tool, add replacing networks and more. Upon running this file, you will be presented with a simple main menu where you select an option by typing a number followed by enter. To start the tool without any input first, run main.py

If you are interested in running the tool continuously using emails or the SpeedSmart API as a trigger, have a look at the following sections.

## FAQ
We have answered a few of the most Frequently asked questions below:

### How do I get started?
Simply follow the basic instructions above and expand with the optional features below.

### What are the *.sst-data files?
These are for the program to know what network names need adding back to the table when we process it. You can manually modify them, but it's easier to use the start.py file to do it for you. It's our own file extension, short for SpeedSmart Tools data.

### Questions about SpeedSmart's new table format
SpeedSmart have changed their export format slightly, between December 2022 and February 2023. Here's what's happened, in order of implemantition:
- Values (e.g. 20.00) are rounded/trimmed (e.g. to 20). This also does slightly reduce longitude/latitude accuracy, but this shouldn't be a problem. WiFi speeds seem to be just zero-trimmed and not rounded. This applies to all exported tables.
- A "Mobile Type" column has been added to exports on the newer app versions.
- "Jitter" and "Notes" columns have been added to tables exported on newer versions of the Android app, and possibly iOS.

I'm not saying any of these changes are bad, in fact the addition of Jitter is cool, but this just causes a few problems as this program was sort of hacked together to work with the old format and there is far too much calling a specific item from a list and knowing which item, for example, the SSID will be.

#### Does the program still work?
Essentially, yes it does. But I'll need to update parts over the coming weeks/months as it was sort of hacked together originally for the old format.

### What should I do with exported tables containing the Notes and Jitter columns?
This is a new SpeedSmart feature applying to tables on newer versions of the app. We will work to support this, but in the meantime columns must be manually removed in Excel or simular before being imported.

### What about the Mobile Type column?
As this program is specifically about WiFi speeds, we decided to delete it from tables we combine. The info in it can easily be gained from the ISP or IP columns, and for any WiFi tests it is "N/A". This column will be detected and deleted when combining tables, but the original and latest files must have it removed.

## Optional features
You can read about the optional features this program comes with below.

### Email System
The speedsmart_email.py file allows this program to automatically receive exported SpeedSmart tables via email and run the necessary actions on them before emailing the user back a full-length, correct table. It is possible to set up this file to run continuously so that you do not need to open a computer every time you export your SpeedSmart table. Only emails sent from the address defined as "fromemail" in the secrets file will be read, everything else will be ignored.

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

If you would rather click a button each time to check for emails manually, you can either run the following two commands in a Python shell:
- import speedsmart_email_function
- speedsmart_email_function.check()

Or, you can start the web app and use the button under the "Quick actions" heading.

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
   
And,     maybe after that, you will find your API key...
    
#### Setup instructions
To get this setup running, just use these commands on a virtual machine or other device that will likely stay on for a large amount of time:
- "python3 speedsmart_api.py &"
- Take note of the process ID shown
- "disown [process-id]" Where [process-id] is the ID you took note of.

After that, you are free to log out of the device in question
Please note that only the two strings in quotes are the commands.

### Average calculations

By default, this program will automatically calculate averages based on network name, ISP, Country and more each time it runs. You can disable this behaviour in the config file if you would like to.
To change which columns averages are calculated for, edit the list in the config file.
There is a bonus parameter that you can calculate averages by, and this is "Year"

### Sorting your table

The program includes support to sort your SpeedSmart table by download and upload speeds as well as the default sorting by date.
To have a go with this, run the start.py file and select the option to sort by either download or upload speed. 
Alternatively, click either of the "Sort" options under the "Quick actions" heading in the web app.
This sorting process does not occur automatically every time the tool runs as it would take too much time.

### Combining tables

If you have multiple tables (e.g. from different devices or people) that you would like to combine into one, add the paths to the tables in the config file and then run start.py and pick option 6.

### Searching the table
If you would like to search the SpeedSmart table (i.e. get a list of all rows containing a specific search string), then just run start.py and choose option 7.
The result can be found in the "Results" directory.

### Web App

This program comes with an easy-to-use Django web app to view key stats and/or perform actions.
To have a go with it, run "python3 speedsmart_web.py runserver --noreload" and then visit "http://localhost:8000" in your device's browser to get started.

### Google Drive Integration

This program can integrate into Google Drive and upload saved tables and averages files there.
To set this up, follow the steps below:

1. Install the PyDrive module using "pip install pydrive". You can skip this if you have already installed everything in requirements.txt
2. Visit the [Google Developers Console](https://console.developers.google.com/) and create a new project if needed.
3. Under API's and Services, enable the "Google Drive API"
4. Under the OAUTH consent screen tab, configure options. You can keep your app in "Testing" mode for now.
5. Under "Credentials", create a "OAuth Client ID" for a Desktop application and download the generated .json file. Rename this to client_secrets.json and add it to the same directory as the speedsmart-tools files.
6. Visit the Google Drive website and create a folder you would like this program to use. Once done, copy the long ID in the address bar.
7. Set drive to 1 in the secrets file and paste your folder ID under "driveid".
8. Run speedsmart_gdrive.py to authorize your Google account.

Please note that once set up, average files will no longer be emailed as they will be uploaded to Drive instead. SpeedSmart tables will continue to be emailed if received via the email address or API.

If you get an error about expired credentials after a while, just delete the "gdrive_credentials.txt" file and repeat step 8.

## Goals/To Do list

I will check items off below once they are completed and functional. 

### Core components
- [x] Get back my full length SpeedSmart table
- [x] Restore the full network names for networks containing & or #
- [x] Get the Count column back in my new combined table

### Useful, but not essential, features
- [x] Automate table exports by using the SpeedSmart API
- [x] Add average calculation as an optional feature to the tool.
- [x] Sort the table by download/upload speed
- [x] Integrate with Google Drive
- [x] Combine multiple tables into one

### Web app

- [x] Create a simple Django webpage with ISP averages and other information obtained from the SpeedSmart table
- [x] Functionality to perform quick actions from the Django page
- [x] Let users download and upload tables in the web app

### Email features (very useful to enjoy the benefits of this program without having a computer at hand)
- [x] Set up the program to receive exported CSV files from SpeedSmart by email (e.g. to a random Gmail address) and send them back to the sender once processed.
- [ ] Functionality to add new &/# replacing networks via specially-formatted email
- [x] What is the most secure way to store email server/address/password on a per-user basis?

### Limitations to overcome
- [x] At the moment, this program will stop being useful after 6000 speedtests. I need a robust plan for continuing to create a full-length table before I hit that limit! (Solution: Make the original.csv file longer than 3000 by using a generated full-length file instead of it if needed.)
- [x] If there are two networks that have been truncated to the same thing by SpeedSmart, we need to differentiate them (e.g. by IP address). Temporary solution: Just add both the networks in question as hashtag networks.
- [ ] The email program seems to crash after running for about a day. Is this a memory limit issue? I need to investigate. No bugs get outputted in log file.

## Important Notice
This program is not created or supported by SpeedSmart or VeeApps in any way. It is just something fun I created that can do cool things to my SpeedSmart table.