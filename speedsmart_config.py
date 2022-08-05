# SpeedSmart tools - Configuration file
# This file contains configuration settings for this program. Make sure they are correct before moving onto other debugging methods.
# The following two options MUST BE CHANGED/VERIFIED before the program can be used

# The path to the file containing your first 3000 speedtests taken with the app
original = "original.csv"

# The path to the file which has been recently exported from SpeedSmart
latest = "latest.csv"

# Lines below this DO NOT need to be changed after installing, but can be if desired.

# The path to the new file that the program will create and write the full-length table to. Please note that if this file exists on your system, the program will write over it.
fulllength = "fulllength.csv"

# The path to the file containing truncated and full-length network names. The default file has some, but you may need to add more using start.py or create a new file if desired.
andnetworks = "&networks.sst-data"

# The path to the file containing network names paired with IP addresses. The default file has some, but you may need to add more using start.py or create a new file if desired.
hashnetworks = "#networks.sst-data"

# A setting to decide whether the count column is restored during the program. 0 = no, 1 = yes
count = 1

# The following setting should be set to 0 if your SpeedSmart table comes out full-length when exported by SpeedSmart. If you have more than 3000 tests or have somehow ended up with two tables with overlap, set it to 1
puttingtogether = 1