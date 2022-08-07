import requests
import speedsmart_secrets as secrets
import json
import csv
import speedsmart_attach
# Please add your SpeedSmart API key in the secrets file before running this.

response = requests.get("https://api.veeapps.com/v1/export_history_json.php?key="+secrets.apikey+"&user=null")
data = response.json()
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
import main
speedsmart_attach.attach_and_send()