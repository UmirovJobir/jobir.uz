from django.urls import path
from .views import my_resume_download_view, contact_view
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    # path('', home),
    # path('', TemplateView.as_view(template_name="app/index.html"), name='home'),
    path('resume/', my_resume_download_view, name='resume'),
    path('', contact_view, name='home'),
]