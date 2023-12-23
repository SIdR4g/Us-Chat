from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('chat.urls')),
    path('admin/', admin.site.urls),
]