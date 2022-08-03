import csv

def restore_full_length(originaltable, latesttable):
    # This function will give you a full-length SpeedSmart table
    with open(originaltable, "r") as ss_original_file:
        with open (latesttable, "r") as ss_latest_file:
            # Remove the headers
            ss_latest_file.readline()
            # Get the first speedtest present in the file
            firsttest = ss_latest_file.readline()
            firsttest = firsttest.split(",").pop(0)
            count = 1
            for row in ss_original_file:
                row = row.split(",").pop(0)
                print(row)
                print(firsttest)
                input()
                if row == firsttest:
                    print("Found first test in original file, row "+count)
                    count += 1
