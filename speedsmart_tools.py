import csv

def restore_full_length(originaltable, latesttable):
    # This function will give you a full-length SpeedSmart table
    with open(originaltable, "r") as ss_original_file:
        with open (latesttable, "r") as ss_latest_file:
            # Get the first speedtest present in the file
            firsttest = list(csv.reader(ss_latest_file))[1]
            firsttest.pop(0)
            print(firsttest)
            count = 1
            inserting = []
            for row in csv.reader(ss_original_file):
                row.pop(0)
                inserting.append(row)
                if row == firsttest:
                    print("Found first test in original file, row ", count)
                    break
                count += 1
    print(inserting)