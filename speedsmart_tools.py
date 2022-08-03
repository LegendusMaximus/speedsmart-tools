import csv

def restore_full_length(originaltable, latesttable, newtablename):
    # This function will give you a full-length SpeedSmart table
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
        ss_latest_file.readline()
        ss_latest_file.readline()
        writing = writing+ss_latest_file.read()
    with open (newtablename, "w") as combinedfile:
        combinedfile.write(writing)
        print("Written full table to "+newtablename)

