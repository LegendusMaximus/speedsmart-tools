# speedsmart-tools
A set of tools to help me export my SpeedSmart table

## About the tools
This set of tools is made specifically for SpeedSmart History files which have been truncated by SpeedSmart (either due to hitting the 3000 speedtests export limit, truncation of network names containing an & character or removal of network names containing a # character). It has been designed to be relatively simple to use, just give it the required files and start it. It outputs a complete file which is useful for data analysis.

## Why is this needed?

This set of tools needs to be created as:
- SpeedSmart for iOS only exports your last 3000 speedtests, and I have more than that. I would like to create a complete table file, and I think others might want to too.
- SpeedSmart will truncate a network name containing the & character, and a program can easily restore those names given a list of what they are supposed to look like (for example, I sometimes speedtest networks called "H&M Free WiFi" and they come through as "H" in SpeedSmart).
- Network names containing a # symbol are not included in the export (i.e. They have a row but the name comes through as "N/A"). It is possible to identify these by IP address and add them back to the file, but this process takes a long time by hand.

## Installation
If you would like to have a go with this on your computer, here is how to get it installed:

1. Download the code as a ZIP file or clone the repository.
2. Edit the speedsmart_config.py file with valid file paths.
3. Rename speedsmart_secrets_example.py to speedsmart_secrets.py and add details.
4. Install the project requirements by using "pip install -r requirements.txt"
5. Run the start.py file to add replacing networks or start the tool. To start the tool without any input first, run main.py

## Goals/To Do list
I will check items off below once they are completed and functional

### Core components
- [x] Get back my full length SpeedSmart table
- [x] Restore the full network names for networks containing & or #
- [x] Get the Count column back in my new combined table

### Email features (very useful to enjoy the benefits of this program without having a computer at hand)
- [ ] Set up the program to receive exported CSV files from SpeedSmart by email (e.g. to a random Gmail address) and send them back to the sender once processed.
- [ ] Add average calculation as an optional feature to the tool. Maybe calculate these if the user includes a certain string in the email they send to the program (e.g. [[averages=true]])
- [ ] Functionality to add new &/# replacing networks via specially-formatted email
- [ ] What is the most secure way to store email server/address/password on a per-user basis?

### Limitations to overcome
- [ ] At the moment, this program will stop being useful after 6000 speedtests. I need a robust plan for continuing to create a full-length table before I hit that limit!
- [ ] If there are two networks that have been truncated to the same thing by SpeedSmart, we need to differentiate them (e.g. by IP address)