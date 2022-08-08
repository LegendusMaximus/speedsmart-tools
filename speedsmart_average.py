import speedsmart_config as config
def country():
    uploads = {}
    averages = {}
    import os
    file = open(config.fulllength)
    header = file.readline()
    for line in file:
        values = line.split('"')
        country = values[21]
        if country not in averages:
            averages[country] = []
        averages[country].append(float(values[9]))
        if country not in uploads:
            uploads[country] = []
        uploads[country].append(float(values[11]))
    lines = "Country,Number of tests taken,Average Download speed MBPS,Average Upload speed MBPS\n"
    for name in averages:
        average = sum(averages[name])/len(averages[name]) 
        uploadaverage = sum(uploads[name])/len(uploads[name])
        line = name+","+str(len(averages[name]))+","+str(average)+","+"\""+str(uploadaverage)+"\""+"\n"
        lines += line
    output=open(config.countryaverage, "w")
    output.write(lines)
    output.close()