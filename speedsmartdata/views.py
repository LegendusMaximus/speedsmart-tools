from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import speedsmart_stats as stats
import speedsmart_average
import speedsmart_config as config
import speedsmart_tools
import os
import shutil
import speedsmart_email_function
import csv

def index(request):
    completed = 0
    if request.method == "POST" and request.FILES["ssfile"]:
        file = request.FILES["ssfile"]
        fs = FileSystemStorage()
        if fs.exists("files/"+file.name):
            fs.delete("files/"+file.name)
        filename = fs.save("files/"+file.name, file)
        print("Program started.")
        speedsmart_tools.restore_full_length(config.original, "files/"+file.name, config.fulllength)
        if config.andnetworks == 0:
            print("Skipping and replacing")
        else:
            print("Starting and replacing")
            speedsmart_tools.and_replacing(config.fulllength)

        if config.hashnetworks == 0:
            print("Skipping hashtag replacing")
        else:
            print("Starting hashtag replacing")
            speedsmart_tools.hashtag_replacing(config.fulllength)

        if config.count == 1:
            print("Restoring count column")
            speedsmart_tools.restore_count(config.fulllength)
        print("Finished!")
        completed = 1
    length = stats.table_length()
    downloadavg, uploadavg, pingavg = stats.average()
    yearaverage = open("averages/Year.csv", "r")
    yearavg = list(csv.reader(yearaverage))
    return render(request, "speedsmartdata/index.html", {"length": length,"downloadavg": downloadavg,"uploadavg": uploadavg, "pingavg": pingavg, "completed": completed, "yearavg": yearavg})

def sortdown(request):
    if request.method == "POST":
        speedsmart_tools.sort_by_speed(0)
        return render(request, "speedsmartdata/sort.html", {"type": "download"})

def sortup(request):
    if request.method == "POST":
        speedsmart_tools.sort_by_speed(1)
        return render(request, "speedsmartdata/sort.html", {"type": "upload"})

def fulllength(request):
    if request.method == "POST":
        return download(config.fulllength)
    else:
        return HttpResponse("This download cannot be completed as it was not initiated through the correct button on the homepage.")

def sorted(request):
    if request.method == "POST":
        return download("sorting/speed.csv")
    else:
        return HttpResponse("This download cannot be completed as it was not initiated through the correct button on the homepage.")

def averages(request):
    if request.method == "POST":
        shutil.make_archive("averages", 'zip', "averages/")
        return download("averages.zip")
    else:
        return HttpResponse("This download cannot be completed as it was not initiated through the correct button on the homepage.")




def download(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/plain")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def email(request):
    if request.method == "POST":
        speedsmart_email_function.check()
        return render(request, "speedsmartdata/email.html")
    else:
        return HttpResponse("The email check needs to be initiated through the correct button on the homepage.")