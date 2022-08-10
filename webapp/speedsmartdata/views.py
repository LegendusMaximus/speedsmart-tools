from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
import stats as stats
import speedsmart_average
import speedsmart_config as config
import speedsmart_tools

def index(request):
    completed = 0
    if request.method == "POST":
        file = request.FILES["ssfile"]
        fs = FileSystemStorage()
        if fs.exists("files/"+file.name):
            fs.delete("files/"+file.name)
        filename = fs.save("files/"+file.name, file)
        print("Program started.")
        if config.puttingtogether == 1:
            speedsmart_tools.restore_full_length(config.original, "files/"+file.name, config.fulllength)
        else:
            print("Temporarily deleting the count column from your table. This will be added back later in the program if requested.")
            speedsmart_tools.delete_count(config.fulllength)
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
    return render(request, "speedsmartdata/index.html", {"length": length,"downloadavg": downloadavg,"uploadavg": uploadavg, "pingavg": pingavg, "completed": completed})