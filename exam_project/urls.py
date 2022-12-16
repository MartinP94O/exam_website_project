from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_project.web.urls')),
    path('profile/', include('exam_project.accounts.urls')),
]
