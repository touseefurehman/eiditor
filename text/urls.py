from django.contrib import admin
from django.urls import path, include  # Import the include function
from editor import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', include('editor.urls')),  # Use include() for app URLs
]
