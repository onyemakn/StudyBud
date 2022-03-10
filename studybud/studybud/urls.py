from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
	return HttpResponse('Home page')
	

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home),

]
