from django.shortcuts import render

# Create your views here.

import pandas as pd, csv, os
from django.http import HttpResponse
from web.settings import BASE_DIR

TEMPLATE_DIRECTORY = "csv"


def index(request, filename):
    html = create_html("{}/{}".format(TEMPLATE_DIRECTORY, filename))
    return HttpResponse(html, content_type="text/html")

def file_list(request):
    file_list = os.listdir("{}/{}".format(BASE_DIR, "csv"))
    return render(request, 'files.html', {'files': file_list})

def create_html(filename):
    df = pd.read_csv(filename)
    return df.to_html()
