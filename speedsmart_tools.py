import csv

def restore_full_length(tablename):
    filename = tablename
    with open(filename, "r") as csvfile:
        datareader = csv. reader(csvfile)
        for row in datareader:
            print(row)
            input()