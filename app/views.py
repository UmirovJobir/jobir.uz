from django.shortcuts import render
from django.http.response import FileResponse
from django.http import JsonResponse

from .forms import GetInTouchForm
from .models import Project


def home_contact(request):
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Thank you for your message! We will get in touch with you soon.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form submission.'}, status=400)
    else:
        form = GetInTouchForm()
        projects = Project.objects.filter(status=True)
    return render(request, 'app/index.html', {'form': form, 'projects': projects})


def my_resume(request):
    return render(request, 'app/resume.html')

def my_resume_download_view(request):
    """The My Resume Download View
        uses for download resume."""
    if request:
        filename = 'static/app/resume.pdf' 
        response = FileResponse(open(filename, 'rb'))

        return response
    
