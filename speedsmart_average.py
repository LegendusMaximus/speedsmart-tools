import speedsmart_config as config
import os
import csv
import speedsmart_average_count as countruns
import speedsmart_attach
import speedsmart_secrets as settings
import shutil
config.fulllength = "combined.csv"
def calculate(type):
    calculatingnum = 0
    uploads = {}
    averages = {}
    file = open(config.fulllength)
    filereader = list(csv.reader(file))
    for rownumber, line in enumerate(filereader):
        if rownumber == 0:
            if type in line:
                for position, part in enumerate(line):
                    if part == type:
                        calculatingnum = position                        
            else:
                print(type+" is not a valid column in "+config.fulllength)
                return "INVALID COLUMN"
        else:
            calculating = line[calculatingnum]
            if calculating not in averages:
                averages[calculating] = []
            averages[calculating].append(float(line[4]))
            if calculating not in uploads:
                uploads[calculating] = []
            uploads[calculating].append(float(line[5]))
    lines = type+",Number of tests taken,Average Download speed MBPS,Average Upload speed MBPS\n"
    for name in averages:
        average = sum(averages[name])/len(averages[name]) 
        uploadaverage = sum(uploads[name])/len(uploads[name])
        line = "\""+name+"\",\""+str(len(averages[name]))+"\",\""+str(average)+"\","+"\""+str(uploadaverage)+"\""+"\n"
        lines += line
    with open ("averages/"+type+".csv", "w") as output:
        output.write(lines) 

def all():
    for columnforcalculating in config.averagelist:
        if columnforcalculating == "Year":
            year()
        else:
            calculate(columnforcalculating)
    if settings.drive == 1:
        shutil.make_archive("averages", 'zip', "averages/")
        import speedsmart_gdrive
        speedsmart_gdrive.upload("averages.zip")
    else:
        if countruns.count >= config.averageemail-1:
            speedsmart_attach.send_averages()
            with open("speedsmart_average_count.py", "w") as file:
                file.write("count = 0")                    
        else:
            writing = countruns.count+1
            with open("speedsmart_average_count.py", "w") as file:
                file.write("count = "+str(writing))

def year():
    with open(config.fulllength, "r") as table:
        reader = list(csv.reader(table))
        for rownum, row in enumerate(reader):
            if rownum != 0:
                row[1] = row[1].split("/")[2].split("-")[0]
    averages = {}
    uploads = {}
    reader.pop(0)
    for line in reader:
        calculating = line[1]
        if calculating not in averages:
            averages[calculating] = []
        averages[calculating].append(float(line[4]))
        if calculating not in uploads:
            uploads[calculating] = []
        uploads[calculating].append(float(line[5]))
    lines = "Year,Number of tests taken,Average Download speed MBPS,Average Upload speed MBPS\n"
    for name in averages:
        average = sum(averages[name])/len(averages[name]) 
        uploadaverage = sum(uploads[name])/len(uploads[name])
        line = "\""+name+"\",\""+str(len(averages[name]))+"\",\""+str(average)+"\","+"\""+str(uploadaverage)+"\""+"\n"
        lines += line
    with open ("averages/Year.csv", "w") as output:
        output.write(lines) 
