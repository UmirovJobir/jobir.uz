from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.http.response import FileResponse
from django.http import JsonResponse

from .forms import GetInTouchForm

def home(request):
    return render(request, 'app/index.html')

def my_resume_download_view(request):
    """The My Resume Download View
        uses for download resume."""
    if request:
        filename = 'static/app/resume.pdf' 
        response = FileResponse(open(filename, 'rb'))

        return response
    
def contact_view(request):
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Thank you for your message! We will get in touch with you soon.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form submission.'}, status=400)
    else:
        form = GetInTouchForm()
    return render(request, 'app/index.html', {'form': form})
