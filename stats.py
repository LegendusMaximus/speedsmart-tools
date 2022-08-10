import speedsmart_tools
import speedsmart_config as config
import csv
from statistics import mean

def table_length():
    with open(config.fulllength, "r") as table:
        treader = list(csv.reader(table))
        lengthoftable = len(treader)-1
    return lengthoftable

def average():
    download_avg = []
    upload_avg = []
    ping_avg = []
    with open(config.fulllength, "r") as table:
        reader = list(csv.reader(table))
        for rowindex, row in enumerate(reader):
            if rowindex != 0:
                download_avg.append(float(row[4]))
                upload_avg.append(float(row[5]))
                ping_avg.append(float(row[6]))
    download_avg = str(mean(download_avg))
    upload_avg = str(mean(upload_avg))
    ping_avg = str(mean(ping_avg))
    return download_avg, upload_avg, ping_avg