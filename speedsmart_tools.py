import csv
import speedsmart_config as config
import speedsmart_average as averages
import operator
import speedsmart_secrets as settings

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
    with open(config.andnetworks, "w") as andfile:
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
        tablereader = list(csv.reader(readtable))
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
    if config.averages == 1:
        print("Starting average calculations")
        averages.all()
        if settings.drive == 1:
            import speedsmart_gdrive
            speedsmart_gdrive.upload(config.fulllength)

def delete_count(table):
    with open(table, "r") as tablefile:
        reader = csv.reader(tablefile)
        readersave = list(reader)
        if readersave[0][0] == "Count":
            for row in readersave:
                row.pop(0)
    with open(table, "w") as writingfile:
        print(readersave)
        writing = ""
        for row in readersave:
            for index, item in enumerate(row):
                writing = writing+"\""+item+"\""
                if index == len(row)-1:
                    writing = writing+"\n"
                else:
                    writing = writing+","
        writingfile.write(writing)

def sort_by_speed(type):
    # 0 sorts by download, 1 sorts by upload
    if type == 0:
        colnum = 4
    else:
        colnum = 5
    with open (config.fulllength, "r") as file:
        reader = list(csv.reader(file))
        for number, row in enumerate(reader):
            if number != 0:
                row[colnum] = float(row[colnum])
        reader.pop(0)
        sortedlist = sorted(reader, key=operator.itemgetter(colnum), reverse=True)
    with open("sorting/speed.csv", "w") as writingfile:
        writing = '"Count","Date & Time","Connection Type","Mobile Type","Download Mbps","Upload Mbps","Ping Ms","Data Used MB","Server","ISP","Country","Latitude","Longitude","Device","Device Name","Network SSID","IP Address"\n'
        for row in sortedlist:
            for index, item in enumerate(row):
                writing = writing+"\""+str(item)+"\""
                if index == len(row)-1:
                    writing = writing+"\n"
                else:
                    writing = writing+","
        writingfile.write(writing)

def combine(tables):
    if len(tables) == 1:
        print("You need two tables or more in the list in the config file to use this feature.")
    for number, table in enumerate(tables):
        if number == 0:
            with open (table, "r") as tablefile:
                writing = tablefile.read()
        else:
            with open(table, "r") as tablefile2:
                t_reader = list(csv.reader(tablefile2))
                t_reader.pop(0)
                for row in t_reader:
                    for index, item in enumerate(row):
                        writing = writing+"\""+item+"\""
                        if index == len(row)-1:
                            writing = writing+"\n"
                        else:
                            writing = writing+","
    with open(config.combined, "w") as writingfile:
        writingfile.write(writing)
