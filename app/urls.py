from django.urls import path
from .views import my_resume_download_view, home_contact, my_resume


app_name = 'app'

urlpatterns = [
    path('', home_contact, name='home'),
    path('resume/', my_resume, name='resume'),
    # path('resume/', my_resume_download_view, name='resume'),
]