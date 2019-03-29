from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

import pandas as pd, csv, os
from django.http import HttpResponse
from web.settings import BASE_DIR

TEMPLATE_DIRECTORY = "csv"

@login_required
def index(request, filename):
    html = create_html("{}/{}".format(TEMPLATE_DIRECTORY, filename))
    return HttpResponse(html, content_type="text/html")

@login_required
def file_list(request):
    file_list = os.listdir("{}/{}".format(BASE_DIR, "csv"))
    return render(request, 'files.html', {'files': file_list})

def create_html(filename):
    df = pd.read_csv(filename)
    return df.to_html()
