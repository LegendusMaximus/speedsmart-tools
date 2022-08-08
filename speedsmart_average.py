import speedsmart_config as config
import os
import csv

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
        calculate(columnforcalculating)