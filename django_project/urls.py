from django.contrib import admin
from django.urls import path, include
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
