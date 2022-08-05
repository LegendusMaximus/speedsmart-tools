# SpeedSmart tools - Configuration file
# This file contains configuration settings for this program. Make sure they are correct before moving onto other debugging methods.
# The following two options MUST BE CHANGED/VERIFIED before the program can be used They do not need to be changed if the puttingtogether setting is set to 0.

# The path to the file containing your first 3000 speedtests taken with the app
original = "original.csv"

# The path to the file which has been recently exported from SpeedSmart
latest = "latest.csv"

# Lines below this DO NOT need to be changed after installing, but can be if desired.

# The path to the new file that the program will create and write the full-length table to. Please note that if this file exists on your system, the program will write over it. If you don't need your table putting back together, this setting should point to your most recent exported table and you should change the puttingtogether setting further down this file to 0.
fulllength = "fulllength.csv"

# The following two settings are for replacing processes in the table. To disable either of these processes completely (e.g. users on a new version of SpeedSmart will not need hashtag replacing), just change their values to 0.

# The path to the file containing truncated and full-length network names. The default file has some, but you may need to add more using start.py or create a new file if desired.
andnetworks = "&networks.sst-data"

# The path to the file containing network names paired with IP addresses. The default file has some, but you may need to add more using start.py or create a new file if desired.
hashnetworks = "#networks.sst-data"

# A setting to decide whether the count column is restored during the program. 0 is no, 1 is yes
count = 1

# The following setting should be set to 0 if your SpeedSmart table comes out full-length when exported by SpeedSmart. If you have more than 3000 tests or have somehow ended up with two tables with overlap, set it to 1
puttingtogether = 1