import csv
import speedsmart_config as config
andnetworks = config.andnetworks

def restore_full_length(originaltable, latesttable, newtablename):
    # This function will save a full-length SpeedSmart table under the specified name
    with open(originaltable, "r") as ss_original_file:
        with open (latesttable, "r") as ss_latest_file:
            # Get the first speedtest present in the file
            firsttest = list(csv.reader(ss_latest_file))[1]
            firsttest.pop(0)
            count = 1
            inserting = []
            for row in csv.reader(ss_original_file):
                row.pop(0)
                inserting.append(row)
                if row == firsttest:
                    print("Found first test in original file, row ", count)
                    break
                count += 1
    writing = ""
    for rowlist in inserting:
        for index, item in enumerate(rowlist):
            writing = writing+"\""+item+"\""
            if index == len(rowlist)-1:
                writing = writing+"\n"
            else:
                writing = writing+","
    with open (latesttable, "r") as ss_latest_file:    
        latesttablelist = []
        for index, row in enumerate(csv.reader(ss_latest_file)):
            if index > 2:
                row.pop(0)
                latesttablelist.append(row)
    for row in latesttablelist:
        for index, item in enumerate(row):
            writing = writing+"\""+item+"\""
            if index == len(row)-1:
                writing = writing+"\n"
            else:
                writing = writing+","
    with open (newtablename, "w") as combinedfile:
        combinedfile.write(writing)
        print("Written full table to "+newtablename)

def add_replacing_network(truncated, full):
    with open(andnetworks, "r") as read:
        text = read.read()
    with open(andnetworks, "w") as andfile:
        andfile.write(text+"\n\""+truncated+"\",\""+full+"\"")
