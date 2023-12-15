from django.shortcuts import render
from django.views.generic import ListView
from django.http.response import FileResponse

# def home(request):
#     return render(request, 'app/index.html')

def my_resume_download_view(request):
    """The My Resume Download View
        uses for download resume."""
    if request:
        filename = 'app/static/resume.pdf'
        response = FileResponse(open(filename, 'rb'))

        return response