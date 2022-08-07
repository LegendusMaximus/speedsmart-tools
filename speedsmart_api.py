import requests
import speedsmart_secrets as secrets
import json
import csv
import speedsmart_attach
import time
import speedsmart_tools
import speedsmart_config as config
# Please add your SpeedSmart API key in the secrets file before running this file.
# This program checks the SpeedSmart API every 3 minutes for new tests. If it finds one, it will then run through all the tools and send out the full-length table via email. After that, it will wait half an hour to prevent spamming of users while they are speedtesting.

lastdata = ""
while True:
    time.sleep(180)
    response = requests.get("https://api.veeapps.com/v1/export_history_json.php?key="+secrets.apikey+"&user=null")
    data = response.json()
    if lastdata != data:
        lastdata = data
        history = data["resultHistory"]
        history.reverse()
        data_file = open("latest.csv", "w")
        csv_writer = csv.writer(data_file)
        count = 0

        for test in history:
            if count == 0:
                header = ["Count","Date & Time", "Connection Type", "Mobile Type", "Download Mbps", "Upload Mbps", "Ping Ms", "Data Used MB", "Server", "ISP", "Country", "Latitude", "Longitude", "Device", "Device Name", "Network SSID", "IP Address"]
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(test.values())
        data_file.close()
        print("Written API response to latest.csv, now beginning program.")
        print("Program started.")
        if config.puttingtogether == 1:
            speedsmart_tools.restore_full_length(config.original, config.latest, config.fulllength)
        else:
            print("Temporarily deleting the count column from your table. This will be added back later in the program if requested.")
            speedsmart_tools.delete_count(config.fulllength)
        if config.andnetworks == 0:
            print("Skipping and replacing")
        else:
            print("Starting and replacing")
            speedsmart_tools.and_replacing(config.fulllength)
        if config.hashnetworks == 0:
            print("Skipping hashtag replacing")
        else:
            print("Starting hashtag replacing")
            speedsmart_tools.hashtag_replacing(config.fulllength)
        if config.count == 1:
            print("Restoring count column")
            speedsmart_tools.restore_count(config.fulllength)
        print("Finished!")
        speedsmart_attach.attach_and_send()
        time.sleep(1800)
    else:
        print("data same as last time, nothing to send right now.")