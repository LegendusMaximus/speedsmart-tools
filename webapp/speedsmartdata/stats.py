import speedsmart_tools
import speedsmart_config as config
import csv

def table_length():
    with open(config.fulllength, "r") as table:
        treader = list(csv.reader(table))
        lengthoftable = len(treader)-1
    return lengthoftable