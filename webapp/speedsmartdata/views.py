from django.shortcuts import render
from django.http import HttpResponse, Http404
import stats

def index(request):
    length = stats.table_length()
    return render(request, "speedsmartdata/index.html", {"length": length})