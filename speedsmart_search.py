import os
import csv
import speedsmart_config as config

lines = ""
results = 0
file = open(config.fulllength)
search = input("Enter text to search SpeedSmart table")
for line in file:
	if search in line:
		lines += line
		results += 1
if lines == "":
	print("No results for", search)

else:
	print("There are", results, "results for", search)
filenamingsystem = f"ResultsFor{search}_{results}.csv"
filename = "results/"+filenamingsystem
output = open(filename, "w")
output.write(lines)
output.close()