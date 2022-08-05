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
def add_hashtag_network(name, ip):
    with open(config.hashnetworks, "r") as read:
        text = read.read()
    with open(config.hashnetworks, "w") as hashfile:
        hashfile.write(text+"\n\""+name+"\",\""+ip+"\"")

def hashtag_replacing(table):
    ips = []
    names = []
    table2 = table
    with open(config.hashnetworks, "r") as hashnetworks:
        with open(table, "r") as table:
            tablereader = list(csv.reader(table))
            hashreader = list(csv.reader(hashnetworks))
            for row in hashreader:
                names.append(row[0])
                ips.append(row[1])
            for row in tablereader:
                ip = row[15]
                if ip in ips:
                    for index, ipadr in enumerate(ips):
                        if ipadr == ip:
                            row[14] = names[index]
    writing = ""
    for row in tablereader:
        for index, item in enumerate(row):
            writing = writing+"\""+item+"\""
            if index == len(row)-1:
                writing = writing+"\n"
            else:
                writing = writing+","
    with open (table2, "w") as combinedfile:
        combinedfile.write(writing)

def and_replacing(table):
    truncatednames = []
    names = []
    table2 = table
    with open(config.andnetworks, "r") as andnetworks:
        with open(table, "r") as table:
            tablereader = list(csv.reader(table))
            andreader = list(csv.reader(andnetworks))
            for row in andreader:
                truncatednames.append(row[0])
                names.append(row[1])
            for row in tablereader:
                truncatedname = row[14]
                if truncatedname in truncatednames:
                    for index, truncatedname2 in enumerate(truncatednames):
                        if truncatedname2 == truncatedname:
                            row[14] = names[index]
    writing = ""
    for row in tablereader:
        for index, item in enumerate(row):
            writing = writing+"\""+item+"\""
            if index == len(row)-1:
                writing = writing+"\n"
            else:
                writing = writing+","
    with open (table2, "w") as combinedfile:
        combinedfile.write(writing)

def restore_count(table):
    with open (table, "r") as readtable:
        tablereader = list(csv.reader(table))
        tablelen = len(tablereader)-1
        tablereader[0].insert(0, "Count")
        for i, row in enumerate(tablereader):
            if i >= 1:
                row.insert(0, str(tablelen))
                tablelen = tablelen-1
                readersave = tablereader
    with open(table, "w") as writingfile:
        writing = ""
        for row in readersave:
            for index, item in enumerate(row):
                writing = writing+"\""+item+"\""
                if index == len(row)-1:
                    writing = writing+"\n"
                else:
                    writing = writing+","
        writingfile.write(writing)

